# wertstromanalyse.html – Änderungen (Toolkit)

Alle Fixes im Code mit `// FIX (Toolkit): …` bzw. `/* FIX (Toolkit): … */` markiert. IDs, Datenformat (`params`, `variants`, `ist`/`soll` mit `nodes[]` …), localStorage-Schlüssel (`wertstromW2T3.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) bleiben unverändert. Die Kennzahlen wurden geprüft und nicht verändert: Kundentakt = Betriebszeit ÷ Bedarf, Bearbeitungszeit = Σ ZZ, Liegezeit = Σ Reichweiten, DLZ = Liegezeit + BZ ÷ Betriebszeit, Flussgrad = BZ ÷ DLZ in Sekunden.

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Szenarien, die unter „Austarierung als Szenario festhalten“ eingefroren wurden, gingen beim Speichern verloren. Nach dem Neuladen oder Öffnen der Analyse war die Liste leer. Wurde nur ein Szenario angelegt, galt der Stand außerdem nicht als geändert, er ließ sich also gar nicht speichern. | Die Szenarien liegen als `ist._scen` / `soll._scen`. `A.shape()` verwirft beim Laden alle Schlüssel mit „_“, und `A.cmp()` ignoriert sie beim Änderungsvergleich. Das ist für interne Merker wie `_base` und `_sollTouched` gedacht, traf aber auch diesen Nutzerinhalt. | `_scen` ist von beiden Filtern ausgenommen. Im Vergleich zählt es nur, wenn die Liste nicht leer ist (`renderProblems()` legt sonst bei jeder Vorlage ein leeres `_scen` an). Gespeicherte Projekte bleiben kompatibel: Das Feld kommt nur hinzu. | Auf `main` reproduziert: Szenario einfrieren → speichern → neu laden ergab `_scen = []`. Nach dem Fix bleibt das Szenario erhalten. Alle 5 Vorlagen gelten nach dem Laden weiterhin als unverändert. Ein eingefrorenes Szenario allein markiert den Stand jetzt als geändert. |
| 2 | Enthielt ein Prozess- oder Bestandsname „-->“ (z. B. „A-->B“), ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren. | „-->“ beendete den Kommentar `<!-- tool-state: … -->` vorzeitig. | In `stateComment()` wird `>` als `>` geschrieben (gültiges JSON, ältere Exporte laden weiterhin). Gleiche Lösung wie in Gruppe C. | Auf `main` reproduziert (JSON-Fehler). Nach dem Fix laden alle drei Formate den Stand wieder. |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler oder -warnungen.
- Alle 5 Beispiele geladen. Kennzahlen gegen die Musterlösungen bzw. Handrechnung geprüft:
  - Stanz AG IST: Takt 60 Sek, BZ 188 Sek, Liegezeit 23,6 Tage (wie im Video). SOLL: 7 Tage.
  - Pumpenwerk: Takt 115 Sek, BZ 400 Sek.
  - Bäckerei: Takt 23 Sek.
  - Aufgabe 1 (A–B–C): Takt 270 Sek, BZ 105 Sek, IST 8 Tage, SOLL 2 Tage.
  - Leer: Takt 112,5 Sek.
- Konsistenz-Checks und „Offene Probleme“ je Beispiel plausibel (Engpass über Takt, Push, große Puffer, Losgröße > Bedarf bei Aufgabe 1).
- Geführter Aufbau Schritte 1–5, die 7 Fragen, IST ↔ SOLL einschließlich „IST als Ausgangspunkt übernehmen“, Zykluszeit live ändern (Balancing-Diagramm, Flags), geführter Modus bis „fertig“, Tabs FAQ, Legende und Quiz.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel. Der Re-Import aller drei Formate ergibt jeweils exakt den bereinigten Stand. Der Import einer exportierten JSON über den echten `#importFile`-Handler funktioniert.
- Speichern → Neuladen → Öffnen ergibt einen identischen Stand, jetzt einschließlich der Szenarien.
- Quiz: eine komplette Runde mit 20 Fragen bis zur Auswertung, ohne Fehler.
- Layout bei 375 px und 1920 px in allen Tabs: kein horizontaler Seiten-Scroll, keine abgeschnittenen Elemente. Die Karte scrollt in ihrem Container.

## Auffällig, aber nicht geändert

- „Offene Probleme & Lösungen“ und „Linienbalancing“ im Markdown- und Obsidian-Export stammen aus dem hinterlegten Beispiel und folgen nicht den aktuellen Eingaben. Im Tool selbst werden sie live berechnet.
- Szenarien merken sich die Zykluszeiten pro Knotenposition. Nach einem Umsortieren der Prozesse greifen sie auf andere Knoten.
- Beim Umschalten eines Bestands zwischen „in Tagen“ und „in Stück“ wird ein Wert 0 als 1 Tag übernommen.
