# CTQ-Analyse – Änderungsprotokoll

*CTQ analysis – change log.* Phase 1 · Define · Definieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ctq-analyse-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ctq-analyse.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `ctq-analyse-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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
| 1 | Speicher voll: keine Warnung, Speichern-Dialog bleibt stumm offen; danach bleibt Speichern bis zum Neuladen gesperrt („Browser-Speicher nicht verfügbar"), auch wenn wieder Platz ist. | `safeSet()` setzte bei jedem Fehler `storeOK=false`; `showStorageFullWarning()` brach deshalb sofort ab (`if(!storeOK) return`) und setzte selbst ebenfalls `storeOK=false`. | `safeSet()` meldet nur noch `false`; `showStorageFullWarning()` zeigt Toast + Status ohne `storeOK` zu verändern. | Quota-Fehler simuliert: Toast „Speicher voll …", Status „⚠ Speicherfehler"; nach Freigabe klappt das Speichern sofort. |
| 2 | Nach dem Wechsel über das Auswahlfeld bzw. „Laden" im Projektdialog steht weiter „noch nicht gespeichert" (Punkt, Verlassen-Warnung), obwohl die Änderungen verworfen wurden. | `loadKey()` rief nur `updateDirtyUI()` statt den Zustand zurückzusetzen. | `if(!silent) clearDirty();` | Nach Wechsel `dirty=false`, Status leer. |
| 3 | „Laden" im Projektdialog verwirft ungespeicherte Änderungen ohne Rückfrage. | Anders als im Auswahlfeld fehlte die Abfrage. | Gleiche `confirm`-Abfrage wie beim Auswahlfeld. | Abbrechen → Stand bleibt; Bestätigen → Projekt geladen. |
| 4 | Beim Öffnen einer Vorlage werden Schwelle und CTQ-Auswahl aus Abschnitt 4 vom vorher geöffneten Projekt übernommen (z. B. 95 % statt 80 % → andere Grenzvorschläge). | `loadKey()` setzte `spec` nur für Projekte, nicht für Vorlagen (`loadExample()` tat es). | `spec=ensureSpec(null)` im Vorlagen-Zweig. | Nach Wechsel `thr=80`. |
| 5 | Wiederhergestellter Arbeitsstand (nach Absturz/Schließen) gilt als gespeichert; der Entwurf wird gelöscht – schließt man erneut ohne Änderung, ist die Arbeit weg. | `init()` rief am Ende immer `clearDirty()` (löscht den Entwurf). | Flag `fromDraft`; nach Wiederherstellung aus dem Entwurf `markDirty()`. | Entwurf simuliert → nach `init()` Daten da, `dirty=true`, Status „noch nicht gespeichert". |
| 6 | Markdown-/Obsidian-Export: Zeilenumbrüche aus den mehrzeiligen Feldern (Messmethode, Treiber, Anforderung, Merkmal, Bedürfnis) zerbrechen Tabelle/Baum; beim Import gehen Messmethoden und Grenzen verloren bzw. werden anderen CTQs zugeordnet. | Text wurde ungefiltert in zeilenbasierte Formate geschrieben. | Helfer `L1()` macht Zeilenumbrüche in Tabellenzellen, Baumzeilen, Überschriften und VoC-Zeilen zu Leerzeichen; Obsidian-Callouts setzen `> ` vor jede Zeile (Umbrüche bleiben erhalten). | Methode „Zeile1\nZeile2" → Rückimport „Zeile1 Zeile2", alle Grenzen korrekt zugeordnet. |
| 7 | Importierte Datei wird als Projekt mit den Abschnitt-4-Einstellungen der vorher offenen Analyse gespeichert. | `applyImport()` speicherte `importedSpec||spec` (aktuelle), lud aber `ensureSpec(importedSpec||null)`. | Projekt erhält ebenfalls `ensureSpec(importedSpec||null)`. | Gespeichertes `spec` entspricht dem geladenen (thr 80). |

#### Geprüft ohne Befund
- Alle 5 Vorlagen, Leitfaden-Schritte 1–4 inkl. Unterpunkte (`showStep`), kein `undefined`/`NaN`.
- CTQ-Baum: Treiber/Anforderung/CTQ hinzufügen und löschen; Matrix: Zahlen mit Komma, ungültige Eingaben und Widersprüche werden rot markiert, Fehlerdefinition und Qualitätsziel korrekt.
- Abschnitt 4: CTQ wählen, Messpunkte hinzufügen/löschen, Schwelle, Vorschlag übernehmen, Überblick „Alle".
- Geführter Modus inkl. Abschluss und „ergänzen"; Spezifikations-Chip springt in die Matrix.
- `buildMarkdown()`, `buildJSON()`, `buildObsidian()` je Vorlage; Rückimport aller drei Formate identisch.
- Speichern, Umbenennen, Neuladen aus localStorage. HTML-Escaping (kein Script ausgeführt). FAQ, Quiz (73 Fragen, komplette Runde). Keine Konsolenfehler.

#### Auffällig, nicht geändert
- Mermaid-Mindmap im Obsidian-Export: leere Treiber-/Anforderungsnamen ergeben leere Knoten (Mermaid-Fehler in Obsidian). Randfall.
- Baumzeile im Markdown: ein Merkmal mit `**` oder ` → ` im Namen würde beim Rückimport falsch zerlegt. Randfall.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [ctq-analyse-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ctq-analyse-v1.0.0) verfügbar.
