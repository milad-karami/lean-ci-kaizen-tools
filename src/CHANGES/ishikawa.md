# ishikawa.html – Änderungen (Toolkit)

Alle Fixes im Code mit `/* FIX (Toolkit): … */` markiert. IDs, Datenformat (`problem`, `cats[]` mit `causes[]` und der Warum-Kette `subs[]`), localStorage-Schlüssel (`ishikawaW1T3.v1.*`), Exportstruktur, die eingebetteten Bibliotheken (draw.io, bpmn-js), die CSP und alle Credits (John Naska, mokka.solutions, Quellen) bleiben unverändert.

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Beim Import eines eigenen JSON-Exports wurden alle Warum-Ketten (5-Why) zu „[object Object]“. Bei jedem Beispiel mit Unterursachen ging der Inhalt verloren. | `buildJSON()` exportiert `unterursachen` als Objekte `{t, subs}`, `importJSON()` wandelte aber jeden Eintrag mit `String(x)` in Text um. | Die Einträge werden unverändert übernommen. `ensureShape()` bzw. `whyNorm()` bereinigt sie ohnehin und akzeptiert weiterhin auch reine Texte aus älteren Exporten. | Auf `main` reproduziert (5 von 6 Beispielen enthielten nach dem Import „[object Object]“). Nach dem Fix ergibt der JSON-Re-Import für alle 6 Beispiele exakt den Ausgangsstand, auch bei einer 5-stufigen Warum-Kette. |
| 2 | Bei einem mehrzeiligen Problem (das Problemfeld erlaubt Zeilenumbrüche) übernahm der Re-Import des Markdown- und Obsidian-Exports nur die erste Zeile. | Markdown: Der Importer las nur die Zeile mit `**Problem:**`. Obsidian: Nur die erste Zeile stand im `> [!question]`-Callout, der Importer liest aber nur Callout-Zeilen. | Markdown-Import: Folgezeilen bis zur ersten Kategorie (`## `) werden mitgenommen. Obsidian-Export: Jede Zeile des Problems wird mit `> ` geschrieben. | Auf `main` reproduziert („Zeile eins\nZeile zwei“ → „Zeile eins“). Nach dem Fix übernehmen Markdown, Obsidian und JSON das Problem vollständig. Einzeilige und leere Probleme verhalten sich wie zuvor. |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler oder -warnungen, auch keine CSP-Verletzungen.
- Alle 6 Vorlagen über `loadKey` bzw. die Auswahl geladen. Die Fischgräte wird mit Gräten, Kategorien und Kopf gezeichnet.
- Ursache hinzufügen, Warum-Kette ergänzen, Favorit und Wahrscheinlichkeit setzen, Kategorie hinzufügen und löschen, Kategorien-Vorlagen (6M/8M …), Zoom (+, −, Einpassen, 100 %), Vollbild mit Esc, geführter Modus bis „fertig“, Tabs FAQ, Quiz und Netz.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel. Der Re-Import aller drei Formate (auch in der über `WB.mdExport` erzeugten Download-Fassung) ergibt jeweils exakt `problem` und `cats`. Der Import über den echten `#importFile`-Handler legt eine Analyse „… · Import“ an.
- Speichern bzw. Auto-Anlegen → Autosave → Neuladen → Öffnen ergibt einen identischen Stand.
- Quiz: eine komplette Runde mit 20 Fragen (Auswahl, Reihenfolge, Zuordnung) bis zur Auswertung, ohne Fehler.
- Layout bei 375 px und 1920 px in allen Tabs: kein horizontaler Seiten-Scroll, keine abgeschnittenen Elemente. Die Fischgräte scrollt bzw. zoomt in ihrem Container.

## Auffällig, aber nicht geändert

- Der JSON-Export enthält keine manuell verschobenen Kategoriepositionen (`dx`/`dy`). Nach einem JSON-Import steht die Fischgräte wieder in der Standardanordnung. Die Projektablage und der HTML-Export behalten die Positionen.
- Leerzeichen am Zeilenende innerhalb eines mehrzeiligen Problems werden beim Markdown-Import entfernt.
