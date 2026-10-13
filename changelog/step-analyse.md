# STEP- / PEST-Analyse – Änderungsprotokoll

*STEP / PEST analysis – change log.* Phase 0 · Kontext & Strategie

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.0** | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/step-analyse-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/step-analyse-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/step-analyse-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/step-analyse.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/step-analyse-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `step-analyse-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`variant`, `object`, `factors{KAT:[{t,kind,impact,impl,measure}]}`), localStorage-Schlüssel (`stepW1T4.v1:*`, `stepQuiz.v1`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Enthielt ein Faktor, eine Bedeutung oder eine Maßnahme „-->“ (z. B. „Preis --> runter“), ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr laden („Unterminated string in JSON“). | `-->` im JSON beendete den `<!-- tool-state: … -->`-Kommentar vorzeitig. | In `stateComment()` wird `-->` als `-->` geschrieben. Das ist gültiges JSON, alte Exporte laden weiterhin. | Vorher: Fehler beim Import. Nachher: Markdown und Obsidian mit `A --> B <!-- c -->` und `x-->y` → Import ergibt exakt `state`. |
| 2 | Obsidian-Mindmap: Bei Chancen und Risiken zeigte der Knoten nur „+“ bzw. „-“, der Faktorname fehlte. | `Faktor (+)` ist in Mermaid-Mindmaps die Syntax `id(Text)` (abgerundeter Knoten mit Text „+“). | Suffix ohne Klammern: `Faktor +` / `Faktor -`. Neutrale Faktoren bleiben unverändert. | Ausgabe geprüft: „Deutsches Street-Food als Trend +“. |

#### Was getestet wurde (headless Chrome, `cdp.mjs`)

- Laden ohne Konsolenfehler. Alle 6 Vorlagen über `loadExample()` geladen, Leitfaden-Schritte 1–5 per `showStep()`.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jede Vorlage ohne NaN/undefined. Der Re-Import von Markdown und JSON ergibt jeweils exakt `state`.
- Geführter Modus bis „fertig“ (Zusammenfassung). Tabs FAQ und Quiz. Eine komplette Quizrunde (20 Fragen inkl. Zuordnungsfragen) mit Auswertung, „Fehler üben“ und „Neue Runde“.
- Speichern unter → Autosave nach Änderung → Neuladen (iframe, gleicher localStorage). Ungespeicherter Entwurf wird beim Neuladen wiederhergestellt und bleibt als ungesichert markiert. Projektliste: Löschen → Papierkorb → Wiederherstellen.
- Schmale Ansicht (iframe 375 px): kein horizontales Überlaufen.

#### Auffällig, aber nicht geändert

- Nach „Speichern“ und erneutem Öffnen startet das Tool mit der Standardvorlage. Die gespeicherte Analyse steht in der Auswahlliste. Das ist im gemeinsamen Speichermodul so angelegt (gleich in SWOT).
- `A.shape()` begrenzt `impact` auf 0–5, die Oberfläche kennt nur 1–3. Eine Datei ohne `impact` wird mit 0 („—“) geladen. Das betrifft nur handbearbeitete Dateien.
- Die FAQ-Suche nach „amp“, „lt“ o. Ä. hebt Teile von HTML-Entitäten hervor. Das ist rein optisch.
- Ein „-->“ im Faktortext landet unverändert in der Mermaid-Mindmap, weil `mmClean` `<`/`>` nicht entfernt. Das war schon vorher so.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [step-analyse-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/step-analyse-v1.0.0) verfügbar.
