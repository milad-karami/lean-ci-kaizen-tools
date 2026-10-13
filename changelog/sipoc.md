# SIPOC – Änderungsprotokoll

*SIPOC – change log.* Phase 1 · Define · Definieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/sipoc-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/sipoc.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `sipoc-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Import einer exportierten Markdown-/Obsidian-Datei scheitert („Datei konnte nicht gelesen werden"), sobald irgendein Feld `-->` enthält (z. B. „A --> B" im Warum-Text). | `stateComment()` schreibt den Zustand als JSON in einen HTML-Kommentar; `-->` im Nutzertext beendet den Kommentar vorzeitig, `JSON.parse` bricht ab. | `>` im JSON als `>` maskieren (bleibt gültiges JSON, Import unverändert). | Headless Chrome: `importFromText(buildMarkdown()/buildObsidian())` mit `-->` im Text → Zustand identisch (vorher Exception). |
| 2 | Markdown-Export: die SIPOC-Tabelle bekommt zusätzliche Spalten, wenn ein Schritt/Input/Lieferant/Output/Kunde ein `\|` enthält. | Zellen wurden unmaskiert in die Pipe-Tabelle geschrieben. | `\|` in Tabellenzellen als `\|` maskieren (Helfer `tc`). | Zeile mit „x\|y" hat wieder genau 5 Spalten. |

#### Geprüft ohne Befund
- Laden aller 4 Vorlagen (über Auswahlfeld/`openKey` und Fallkarten), alle 9 Phasen über Stepper und Vor/Zurück, kein `undefined`/`NaN` im UI.
- Schritte hinzufügen/löschen/verschieben (Scope-Auswahl wandert mit), Aussagen, Inputs/Outputs, Lieferanten-/Kunden-Auswahlliste (▾), Live-Diagramm, Qualitätsprüfung.
- `buildMarkdown()`, `buildJSON()`, `buildObsidian()` für jedes Beispiel; Rückimport aller drei Formate ergibt den identischen Zustand.
- Speichern unter (Projekt), Neuladen aus localStorage, Entwurf-Wiederherstellung nach „Absturz" (`bootStore`).
- HTML-Escaping: `<img onerror>` in allen Feldern wird nicht ausgeführt.
- FAQ (Suche, Filter, alle öffnen/schließen), Quiz (alle 55 Fragen strukturell geprüft, komplette Runde mit richtigen/falschen Antworten, „Fehler üben").
- Keine Konsolenfehler.

#### Auffällig, nicht geändert
- `loadExample(id)` wird von der Oberfläche nicht verwendet (Altfunktion, nur vom Test-Harness genutzt). Sie setzt das Auswahlfeld auf `id` statt `ex:id` (Feld wirkt leer) und lässt `curKey` unverändert.
- `renderWizDone()` endet mit einem frühen `return`; der Rest ist toter Code (enthält eine fehlerhafte Scope-Abfrage `scopeSel.indexOf(x.id)`), wirkt sich aber nicht aus.
- Mehrzeilige Texte (Beschreibung, Start/Stop) erscheinen im Markdown als Fortsetzungszeilen der Listenpunkte – darstellungstechnisch unschön, Rückimport funktioniert (Zustand im Kommentar).

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [sipoc-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/sipoc-v1.0.0) verfügbar.
