# SWOT-Analyse (inkl. TOWS) – Änderungsprotokoll

*SWOT analysis (incl. TOWS) – change log.* Phase 0 · Kontext & Strategie

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/swot-analyse-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/swot-analyse.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `swot-analyse-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`object`, `S/W/O/T[]`, `tows{SO,ST,WO,WT}`), localStorage-Schlüssel (`swotW1T4.v1:*`, `swotQuiz.v1`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Mehrzeilige TOWS-Strategien (Textfeld) wurden beim Re-Import von Markdown/Obsidian nach der ersten Zeile abgeschnitten. | Der Export schrieb Folgezeilen ohne Einrückung, der Import las nur `- [ ] …`-Zeilen. | Der Export rückt Folgezeilen um 2 Leerzeichen ein, so bleiben sie auch in Markdown/Obsidian Teil des Listenpunkts. Der Import hängt eingerückte Zeilen an die vorherige Strategie an. | „Zeile 1\n\n  eingerückt\nZeile 4“ und eine zweite mehrzeilige Strategie → Markdown und Obsidian → Import identisch. Alle Vorlagen importieren weiter identisch. |

#### Was getestet wurde (headless Chrome, `cdp.mjs`)

- Laden ohne Konsolenfehler. Alle 5 Vorlagen, Leitfaden-Schritte 1–4.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jede Vorlage ohne NaN/undefined. Der Re-Import aller drei Formate ergibt exakt Objekt, S/W/O/T und TOWS.
- Einträge und Strategien hinzufügen/löschen. Die TOWS-Kopfzeilen werden beim Tippen nachgeführt. HTML im Eintrag wird maskiert (`&lt;b&gt;`). Die Auswertung zählt korrekt.
- Geführter Modus Schritte 1–5 bis „fertig“. Tabs FAQ und Quiz. Eine komplette Quizrunde (20 Fragen inkl. Zuordnungsfragen) mit Auswertung, „Fehler üben“ und „Neue Runde“.
- Speichern, Autosave, Neuladen (iframe), Entwurf bleibt ungesichert markiert, Projektliste (Löschen/Papierkorb/Wiederherstellen). Schmale Ansicht (iframe 375 px): kein horizontales Überlaufen. Die Achsen-Raster haben eine eigene Media-Query bei 720 px.

#### Auffällig, aber nicht geändert

- Wird ein Eintrag in ① gelöscht, verschieben sich die Nummern (S1, S2 …). Bestehende TOWS-Texte wie „S2+O1“ zeigen dann auf andere Faktoren. Das ist im Konzept so angelegt.
- Eine Five-Forces-Datei lässt sich nicht direkt importieren (siehe five-forces.md). Die Übergabe ist manuell.
- Nach „Speichern“ und erneutem Öffnen startet das Tool mit der Standardvorlage. Die Analyse steht in der Auswahlliste (gemeinsames Speichermodul, wie STEP).
- Leere Einträge zählen in Auswertung und Zusammenfassung mit.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [swot-analyse-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/swot-analyse-v1.0.0) verfügbar.
