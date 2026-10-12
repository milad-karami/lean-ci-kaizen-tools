# epei-rechner.html – Änderungen (Toolkit)

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`label`, `p{…}`, `products[]`), localStorage-Schlüssel (`epeiW2T3.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert. Die Rechenlogik (EPEI = n × Rüstzeit ÷ freie Kapazität, Planintervall aufgerundet, Losgröße = Bedarf × EPEI-Plan, Supermarkt = Bedarf × (EPEI-Plan + Sicherheit)) wurde geprüft und nicht verändert.

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Gespeicherte Berechnungen mit 4 oder mehr Schichten (z. B. 4 × 360 min) wurden beim Laden still auf 3 Schichten gesetzt, und alle Ergebnisse änderten sich. | `A.shape()` begrenzte `shifts` auf 1–3 und rundete, obwohl Eingabefeld und Gantt (`shiftLabels`) mehr Schichten zulassen. | Grenze 1–24, keine Rundung beim Laden. Der Gantt rundet für die Schichtanzeige weiterhin selbst. | shifts = 4 → Speichern → Store neu laden → `openKey` ergibt 4 (vorher 3). |
| 2 | Wurde eine Datei mit ungültigen Daten importiert (z. B. JSON mit `_state` ohne `p`), überschrieb das den Stand (`DATA=A.shape(s)\|\|s`), `renderAll()` brach ab und das Tool blieb kaputt. | Bei ungültigen Daten griff der Fallback auf die Rohdaten. | `applyImport()` wirft einen Fehler, bevor `DATA` überschrieben wird. Der bestehende Handler zeigt dann „Datei konnte nicht gelesen werden“. | Über den echten `#importFile`-Handler getestet: Meldung erscheint, der bisherige Stand bleibt erhalten. |
| 3 | Enthielt ein Variantenname „-->“, ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren (JSON-Fehler). | `-->` beendete den `<!-- tool-state: … -->`-Kommentar vorzeitig. | `>` wird im State-Kommentar als `\u003e` geschrieben (gültiges JSON, alte Exporte laden weiterhin). | Name `…\|x-->y` → Markdown-Export → Import ergibt identischen Stand. |
| 4 | Ein „\|“ im Variantennamen zerbrach die Markdown-Tabelle „Produktspektrum“. | Der Zellinhalt wurde nicht maskiert. | `\|` wird als `\\|` maskiert. | Exportzeile geprüft. |
| 5 | Die Abschlusszusammenfassung des geführten Modus zeigte englische Dezimalpunkte („5.0 h“, „8.7 h“, „4.0 Tage“). | `toFixed(1)` statt der Formatfunktion `de()` des Tools. | `de()` verwenden. | Leer-Vorlage: „5 h · 8,7 h · 1 Tage“. |

## Was getestet wurde (headless Chromium über Playwright, `file://`, 1400 px und 375 px)

- Laden ohne Konsolenfehler. Alle 4 Beispiele geladen, Rechenweg-Schritte 1–6 gerendert.
- Werte gegen Handrechnung geprüft, z. B. Fräse: Betriebszeit 1.440, Pausen 90, Störungen 144, Laufzeit 1.140 → frei 66 min, Rüsten 240 min, EPEI 3,64 → 4 Tage, Rüsten Ø 60, Puffer 6 min/Tag, Supermarkt 6 Tage, Auslastung 95,4 %. Losgrößen 2.400/1.440/480/240 wie im Video.
- Engpass (Bedarf A = 2000): EPEI ∞, Banner „Kapazitätsengpass“, Losgröße/Supermarkt „—“, JSON-Felder `null`, Gantt-Hinweis statt Grafik.
- Rüstzeit 0: EPEI 0, Plan 1 Tag, keine Division durch 0.
- Leerer Bedarf → 0. Varianten hinzufügen und löschen (das Löschen der letzten Variante ist nicht möglich).
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel ohne NaN/undefined/Infinity. Der Re-Import aller drei Formate ergibt jeweils exakt `DATA`.
- Geführter Modus bis „fertig“, Tabs FAQ und Quiz. Speichern/Laden, Entwurf und `buildStandaloneHtml()` geprüft.
- Escaping: HTML im Variantennamen wird nicht als Markup gerendert (Tabelle, Wertstrom-Skizze, Gantt).
- Jeder Fehler oben wurde im Browser zuerst auf `main` reproduziert und danach im Fix als behoben bestätigt.
- Breite 1400 px und 375 px: alle Beispiele und alle Schritte ohne horizontalen Seiten-Scroll, keine Konsolenfehler.

## Auffällig, aber nicht geändert

- Bei sehr kleiner freier Kapazität (z. B. 0,1 min/Tag) wird das Planintervall sehr groß (2.401 Tage). Der Gantt zeichnet dann ein Wochenraster mit über 7.000 SVG-Elementen (noch flüssig, etwa 25 ms). Bei noch kleineren Werten kann die Darstellung zäh werden.
- „Neue Variante“ benennt nach Anzahl (`Variante ` + Buchstabe). Nach einem Löschen sind doppelte Namen möglich, nach Z folgen Sonderzeichen. Das ist nur kosmetisch.
- Grammatik „1 Tage“ / „EPEI + 1 Tage Sicherheit“ bei Wert 1.
- Bei nur einer Variante zählt die Formel trotzdem 1 Umrüstung je Zyklus (n × Rüstzeit). Das ist dokumentiertes Verhalten des Tools.
- `A.shape` begrenzt `downtimeRate` auf 99 % (UI erlaubt 100 %). Ohne praktische Auswirkung, da es dann ohnehin einen Engpass gibt.
