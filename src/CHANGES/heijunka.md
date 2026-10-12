# heijunka.html – Änderungen (Toolkit)

Alle Fixes sind im Code mit `// FIX (Toolkit): …` markiert. Unverändert bleiben: IDs, Datenformat (`hoursPerDay`, `daysPerWeek`, `weeksPerMonth`, `phase`, `variants[]`, `manualBasic`), localStorage-Schlüssel (`heijunkaW2T3.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen).

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Bei freier Kapazität (Bedarf < Kapazität) wurde im Monat mehr produziert als bestellt. Beispiel „Einfach“ mit Bedarf Typ C = 0: Typ C bekam 1 Stück je Basiswoche, also 3 Stück im Monat statt 0. Beim zufälligen Prüfen von 20.000 Fällen trat das in rund 58 % der Fälle mit freier Kapazität auf. | `computeWeeklyBasic()` gab die freien Slots der Basiswoche an die Varianten mit dem größten Nachkommarest. Waren mehr Slots frei als Varianten mit Rest vorhanden, bekamen auch Varianten ohne Rest oder mit Bedarf 0 ein Stück dazu. Die Ausgleichswoche wird mit `max(0, …)` berechnet, deshalb wurde das Zuviel nie abgezogen. | Aufgerundet wird nur noch, wenn (Wochen − 1) × Basiswoche den Monatsbedarf nicht übersteigt. Reihenfolge (größter Rest, dann größter Bedarf) und die Methode bleiben wie im Original. | Test mit 20.000 Zufallsfällen (1–8 h/Tag, 2–5 Wochen, 1–6 Varianten, Bedarf ≤ Kapazität): Die Monatsmenge stimmt danach für jede Variante genau mit dem Bedarf überein. Vorher waren es 11.655 Fehlfälle, jetzt 0. Im Browser: „Einfach“ mit C = 0 ergibt Basiswoche 21/11/0 und Monat 80/40/0 (vorher 21/11/1 und 80/40/3). |
| 2 | Sonderfall zu 1: Wird ohne Überproduktion aufgerundet, kann der Rest für die Ausgleichswoche größer werden als eine Woche. `distributeEvenly()` schneidet dann Stücke ab, die nicht in die Woche passen. | Die Größter-Rest-Methode rundet jede Variante höchstens um 1 auf. | Nur wenn die Ausgleichswoche sonst überläuft, wird weiter aufgerundet: jeweils die Variante mit dem größten verbleibenden Rest, solange die Basiswoche Platz hat und nichts überproduziert wird. | Derselbe Zufallstest: 0 Fälle mit übervoller Ausgleichswoche (z. B. 54/29/4/3/2/2 bei 4 h × 5 T × 5 W war vorher 22 > 20). |
| 3 | Eine per Drag & Drop umsortierte Basiswoche ging nach dem Speichern und Laden (Vorhaben, Entwurf, Import) verloren, sobald die Woche leere Slots hatte. | `A.shape()` machte aus `null` den Text `"null"` und filterte ihn heraus. Damit passte die Länge nicht mehr zu den Slots je Woche, und `derive()` verwarf die manuelle Reihenfolge. | Leere Slots (`null`) bleiben erhalten. | „Einfach“ (38 von 40 Slots belegt), Stück verschoben → `A.shape` ergibt Länge 40 statt 38. Nach dem Markdown-Re-Import ist `basicManual` = true, die Reihenfolge ist identisch. |
| 4 | Wurde eine Datei mit ungültigen Daten importiert (z. B. JSON mit `_state` ohne `variants`), wurde der Stand überschrieben (`DATA=A.shape(s)\|\|s`), `renderAll()` brach ab und das Tool blieb kaputt. | Bei ungültigen Daten griff der Fallback auf die Rohdaten. | `applyImport()` wirft einen Fehler, bevor `DATA` überschrieben wird. Der bestehende Handler zeigt dann „Datei konnte nicht gelesen werden“. | Über den echten `#importFile`-Handler getestet: Meldung erscheint, der bisherige Stand (3 Varianten) bleibt erhalten. |
| 5 | Enthielt ein Variantenname „-->“, ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren („Unterminated string in JSON“). | `-->` beendete den `<!-- tool-state: … -->`-Kommentar vorzeitig. | `>` wird im State-Kommentar als `>` geschrieben (gültiges JSON, alte Exporte laden weiterhin). | Name `A\|x-->y` → Markdown-Export → Import über `#importFile` ergibt Name, Reihenfolge und Werte identisch. |
| 6 | Ein „\|“ im Variantennamen zerbrach die Tabellen in Markdown und Obsidian. | Der Zellinhalt wurde nicht maskiert. | `mdCell()` maskiert `\|` als `\\|`. | Zeile: `\| A\\|x-->y \| 80 \| 21 \| 17 \|`. |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler. Alle 4 Beispiele über `switchTo('ex:…')` geladen.
- **Rechnung unverändert für alle Beispiele:** Basiswoche, Ausgleichswoche, Wochenmuster, Wartezeit, Rüstwechsel. Für Video, Einfach, Hochmix und Leer ist alles identisch mit `main`. Video-Beispiel: Basiswoche 7/15/5/5/2/1, Ausgleich 7/15/3/3/4/3, Muster `BRBGOBRBYBGORBBRBGOPBBRBGOYBRBBGORB`, Wartezeit 20 → 3 Tage. Die Monatsmenge je Variante entspricht in allen Beispielen dem Bedarf.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel ohne NaN/undefined. Der Re-Import aller drei Formate ergibt jeweils den gleichen Stand.
- Schritte 1–6 bei 1400 px und 375 px ohne horizontalen Seiten-Scroll.
- Jeder Fehler oben wurde zuerst auf `main` reproduziert und danach im Fix als behoben bestätigt.

## Auffällig, aber nicht geändert

- SMED, EPEI und Heijunka öffnen nach einem Neuladen ohne Entwurf immer das Standardbeispiel, nicht das zuletzt gespeicherte Vorhaben. Das Framework hat keinen „zuletzt geöffnet“-Schlüssel, die Vorhaben bleiben in der Auswahl. Das ist so gebaut, kein Fehler.
- Liegt der Bedarf über der Kapazität, schneidet die Rasteransicht weiterhin ab. Das Tool zeigt dafür bereits eine Warnung (Auslastung > 100 %).
