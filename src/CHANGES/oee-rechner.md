# oee-rechner.html – Änderungen (Toolkit)

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`S` mit `dayH`, `plannedH`, `pph`, `vLosses`, `lLosses`, `qLoss` …), localStorage-Schlüssel (`oeeW2T4.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) bleiben unverändert. Die Rechenlogik (V = verfügbare Zeit ÷ GPS, L = genutzte Zeit ÷ verfügbare Zeit, Q = Gutteile ÷ produzierte Teile, OEE = V × L × Q) wurde geprüft. Sie stimmt und wurde nur an der in Fehler 1 beschriebenen Stelle angepasst.

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Eine GPS größer als „Tag gesamt“ wurde angenommen (z. B. Tag 16 h, GPS 20 h). Das Tool zeigte dann OEE 72,5 %, die Zeitkaskade lief über 100 % hinaus (GPS-Balken 125 %). Nach Speichern und Neuladen ergab dieselbe Berechnung 65,6 %. | `calc()` rechnete mit der rohen GPS. `A.shape()` kappt die GPS beim Laden aber auf den Tag, deshalb wichen gespeicherter und angezeigter Stand voneinander ab. | `calc()` begrenzt die GPS auf den Tag (`Math.min(S.plannedH,S.dayH)`), genauso wie `shape()`. Das Eingabefeld wird beim Tippen nicht verändert. | Auf `main` reproduziert (72,5 % → nach Neuladen 65,6 %). Nach dem Fix vor und nach dem Neuladen 65,6 %, Kaskade ≤ 100 %. |
| 2 | Enthielt eine Verlustbezeichnung „-->“ (z. B. „Rüsten --> Störung“), ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren („Datei konnte nicht gelesen werden“). | „-->“ beendete den Kommentar `<!-- tool-state: … -->` vorzeitig, das JSON darin war dann abgeschnitten. | In `stateComment()` wird `>` als `>` geschrieben. Das ist gültiges JSON, ältere Exporte laden weiterhin. Gleiche Lösung wie in Gruppe C. | Auf `main` reproduziert (JSON-Fehler). Nach dem Fix laden Markdown, Obsidian und JSON den Stand wieder vollständig. |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler oder -warnungen.
- Alle 5 Beispiele über die Vorlagenauswahl (`openKey`) geladen. V, L, Q und OEE gegen die Musterlösungen geprüft: Video 81,3 % × 88,5 % × 91,3 % = 65,6 %, KaffeKönig 66,8 %, Kfz-Werkstatt 68,8 %, World Class 94,0 %, leer 100 %. Die „Live-Kontrolle“ zeigt bei jedem Beispiel „✓ entspricht der Musterlösung“.
- Zeiteinheit h ↔ min und Leistungsmodus „Verluste in min“ ↔ „Produzierte Menge“ hin und zurück: Die OEE bleibt gleich (65,6 %), und die Minuten werden korrekt auf die Einzelposten verteilt.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel. Der Re-Import aller drei Formate ergibt jeweils exakt den bereinigten Stand. Der Import einer exportierten Datei über den echten `#importFile`-Handler funktioniert.
- Speichern als Berechnung → Neuladen → Öffnen ergibt einen identischen Stand. Leitfaden-Schritte 1–7, geführter Modus bis „fertig“, Tabs FAQ und Quiz.
- Quiz: eine komplette Runde mit 20 Fragen bis zur Auswertung durchgespielt, ohne Fehler. Die Generatoren (OEE, Faktor V/L/Q) rechnen korrekt.
- Layout bei 375 px und 1920 px in allen Tabs (Tool, FAQ, Quiz): kein horizontaler Seiten-Scroll, keine abgeschnittenen Elemente.

## Auffällig, aber nicht geändert

- Bei GPS > Tag zeigt das Eingabefeld weiterhin den eingegebenen Wert. Gerechnet wird mit dem Tag. Es gibt keinen eigenen Warnhinweis.
- Der Titel im Markdown-Export nutzt immer die Bezeichnung der Vorlage, auch bei gespeicherten Berechnungen.
