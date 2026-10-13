# EPEI-Rechner – Änderungsprotokoll

*EPEI calculator – change log.* Phase 4 · Improve · Verbessern

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/epei-rechner-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/epei-rechner.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `epei-rechner-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
- Sprachumschalter im Kopfbereich (🇬🇧 English / 🇩🇪 Deutsch); die Toolkit-Navigation bleibt in der gewählten Sprache
- PDF-Bericht der Toolkit-Ebene zweisprachig
- Gespeicherte Projekte werden zwischen beiden Sprachen geteilt; Importe akzeptieren deutsche und englische Exporte

## 2.0.0 – Toolkit-Fassung (2026-10-12)

#### Neu in allen Tools (gemeinsame Toolkit-Ebene)
- Einheitliches Design: dunkler Kopfbereich, animiertes Toolkit-Logo, 3D-Illustration (erstellt mit Codex)
- Top-Leiste mit dem Verbesserungsprozess (0 Kontext → 5 Control), aktuelle Phase markiert, Vor/Zurück zum nächsten Tool
- **📄 Bericht (PDF)**: professioneller A4-Bericht mit Deckblatt, Inhaltsverzeichnis, Glossar und Quellen; Abschnitte per Häkchen wählbar
- Hinweis auf diese Fassung, Versionsnummer und Link auf dieses Änderungsprotokoll im Fußbereich
- Werkzeug-Code, Datenformat, Speicherschlüssel und Exporte bleiben kompatibel zum Original

#### Fehlerkorrekturen gegenüber dem Original

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`label`, `p{…}`, `products[]`), localStorage-Schlüssel (`epeiW2T3.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert. Die Rechenlogik (EPEI = n × Rüstzeit ÷ freie Kapazität, Planintervall aufgerundet, Losgröße = Bedarf × EPEI-Plan, Supermarkt = Bedarf × (EPEI-Plan + Sicherheit)) wurde geprüft und nicht verändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Gespeicherte Berechnungen mit 4 oder mehr Schichten (z. B. 4 × 360 min) wurden beim Laden still auf 3 Schichten gesetzt, und alle Ergebnisse änderten sich. | `A.shape()` begrenzte `shifts` auf 1–3 und rundete, obwohl Eingabefeld und Gantt (`shiftLabels`) mehr Schichten zulassen. | Grenze 1–24, keine Rundung beim Laden. Der Gantt rundet für die Schichtanzeige weiterhin selbst. | shifts = 4 → Speichern → Store neu laden → `openKey` ergibt 4 (vorher 3). |
| 2 | Wurde eine Datei mit ungültigen Daten importiert (z. B. JSON mit `_state` ohne `p`), überschrieb das den Stand (`DATA=A.shape(s)\|\|s`), `renderAll()` brach ab und das Tool blieb kaputt. | Bei ungültigen Daten griff der Fallback auf die Rohdaten. | `applyImport()` wirft einen Fehler, bevor `DATA` überschrieben wird. Der bestehende Handler zeigt dann „Datei konnte nicht gelesen werden“. | Über den echten `#importFile`-Handler getestet: Meldung erscheint, der bisherige Stand bleibt erhalten. |
| 3 | Enthielt ein Variantenname „-->“, ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren (JSON-Fehler). | `-->` beendete den `<!-- tool-state: … -->`-Kommentar vorzeitig. | `>` wird im State-Kommentar als `>` geschrieben (gültiges JSON, alte Exporte laden weiterhin). | Name `…\|x-->y` → Markdown-Export → Import ergibt identischen Stand. |
| 4 | Ein „\|“ im Variantennamen zerbrach die Markdown-Tabelle „Produktspektrum“. | Der Zellinhalt wurde nicht maskiert. | `\|` wird als `\\|` maskiert. | Exportzeile geprüft. |
| 5 | Die Abschlusszusammenfassung des geführten Modus zeigte englische Dezimalpunkte („5.0 h“, „8.7 h“, „4.0 Tage“). | `toFixed(1)` statt der Formatfunktion `de()` des Tools. | `de()` verwenden. | Leer-Vorlage: „5 h · 8,7 h · 1 Tage“. |

#### Was getestet wurde (headless Chrome, `cdp.mjs`)

- Laden ohne Konsolenfehler. Alle 4 Beispiele geladen, Rechenweg-Schritte 1–6 gerendert.
- Werte gegen Handrechnung geprüft, z. B. Fräse: Betriebszeit 1.440, Pausen 90, Störungen 144, Laufzeit 1.140 → frei 66 min, Rüsten 240 min, EPEI 3,64 → 4 Tage, Rüsten Ø 60, Puffer 6 min/Tag, Supermarkt 6 Tage, Auslastung 95,4 %. Losgrößen 2.400/1.440/480/240 wie im Video.
- Engpass (Bedarf A = 2000): EPEI ∞, Banner „Kapazitätsengpass“, Losgröße/Supermarkt „—“, JSON-Felder `null`, Gantt-Hinweis statt Grafik.
- Rüstzeit 0: EPEI 0, Plan 1 Tag, keine Division durch 0.
- Leerer Bedarf → 0. Varianten hinzufügen und löschen (das Löschen der letzten Variante ist nicht möglich).
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel ohne NaN/undefined/Infinity. Der Re-Import aller drei Formate ergibt jeweils exakt `DATA`.
- Geführter Modus bis „fertig“, Tabs FAQ und Quiz. Speichern/Laden, Entwurf und `buildStandaloneHtml()` geprüft.
- Escaping: HTML im Variantennamen wird nicht als Markup gerendert (Tabelle, Wertstrom-Skizze, Gantt).
- Shared `smoke.js`: keine Fehler.

#### Auffällig, aber nicht geändert

- Bei sehr kleiner freier Kapazität (z. B. 0,1 min/Tag) wird das Planintervall sehr groß (2.401 Tage). Der Gantt zeichnet dann ein Wochenraster mit über 7.000 SVG-Elementen (noch flüssig, etwa 25 ms). Bei noch kleineren Werten kann die Darstellung zäh werden.
- „Neue Variante“ benennt nach Anzahl (`Variante ` + Buchstabe). Nach einem Löschen sind doppelte Namen möglich, nach Z folgen Sonderzeichen. Das ist nur kosmetisch.
- Grammatik „1 Tage“ / „EPEI + 1 Tage Sicherheit“ bei Wert 1.
- Bei nur einer Variante zählt die Formel trotzdem 1 Umrüstung je Zyklus (n × Rüstzeit). Das ist dokumentiertes Verhalten des Tools.
- `A.shape` begrenzt `downtimeRate` auf 99 % (UI erlaubt 100 %). Ohne praktische Auswirkung, da es dann ohnehin einen Engpass gibt.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [epei-rechner-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/epei-rechner-v1.0.0) verfügbar.
