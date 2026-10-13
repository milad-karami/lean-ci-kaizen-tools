# Ishikawa-Diagramm – Änderungsprotokoll

*Ishikawa diagram – change log.* Phase 3 · Analyze · Analysieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.0** | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ishikawa-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ishikawa-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ishikawa-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ishikawa.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ishikawa-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `ishikawa-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes sind im Code mit `// FIX (Toolkit): …` markiert. Nur die Anwendungsskripte wurden geändert; eingebettete Bibliotheken (draw.io, bpmn-js, Schriften) und die CSP-Meta-Angabe (ohne `'unsafe-eval'`) sind unverändert. IDs, localStorage-Schlüssel (`ishikawaW1T3.v1.*`), Projektdatenformat und Exportstruktur unverändert; Credits unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Kategorien-Vorlage 4M/6M/8M (Werkzeugleiste und geführter Modus) hängt Ursachen an die falsche Gräte: z. B. „Blutproben“ → 6M legt die „Methode“-Ursachen unter „Maschine“, „Messung/Beschriftung“ unter „Methode“ usw. | Übernahme nach Position (`old[i]`) statt nach Kategoriename; der Tooltip verspricht „Ursachen bleiben erhalten, soweit die Kategorie weiter existiert“ | Gemeinsame Funktion `presetCats()` übernimmt Ursachen nach Name (Groß-/Kleinschreibung egal) – für beide Aufrufstellen | Blutproben → 6M: Mensch/Methode behalten ihre Ursachen, keine falsche Zuordnung; Etikett 4M → 6M: Mensch–Methode erhalten; Strg+Z stellt alle Ursachen wieder her |
| 2 | JSON-Export → Import macht aus jeder Warum-Kette „[object Object]“ | Export schreibt `unterursachen` als verschachtelte Objekte `{t,subs}`, `importJSON()` wandelte jedes Element mit `String(x)` um | Rohliste an `ensureShape()`/`whyNorm()` weiterreichen (normalisiert Strings und Objekte); zusätzlich Bewertung `p` beim Laden auf 0–3 begrenzt | Alle 6 Vorlagen: MD-, JSON- und Obsidian-Export re-importiert → Kategorien, Texte, Bewertung, Favoriten und Warum-Ketten identisch (vorher JSON bei 5 von 6 falsch) |
| 3 | Nach „Datei laden …“ holt Strg+Z / Rückgängig den Inhalt der **vorher** geöffneten Analyse in die importierte Analyse | `applyImport()` setzte den Rückgängig-Verlauf nicht zurück (`loadKey()` tut das über `WB.kontext()`) | `WB.kontext()` nach dem Import aufrufen | Vorlage bearbeitet, Datei importiert, geändert, Rückgängig → Stand des Imports (vorher: Text der vorherigen Analyse) |
| 4 | Mehrzeiliges Problem (Fischkopf ist ein Textfeld) verliert beim Re-Import von Markdown/Obsidian alle Zeilen ab der zweiten; im Obsidian-Callout fällt die zweite Zeile aus dem Kasten | Obsidian-Export setzte `> ` nur vor die erste Zeile; Markdown-Import las nur die Zeile mit `**Problem:**` | Obsidian: jede Zeile mit `> ` präfixen; Markdown-Import liest Folgezeilen bis zur Leerzeile | Problem „Zeile 1\nZeile 2“ → MD und Obsidian re-importiert: identisch |

#### Getestet (headless Chrome, keine Konsolenfehler)

- Alle 6 Vorlagen laden; `buildMarkdown()`, `buildJSON()`, `buildObsidian()` je Vorlage ohne NaN/undefined/[object Object]; Roundtrip aller drei Formate sowie der eingebetteten HTML-Kopie (`buildStandaloneHtml()` → `importFromText()` → `applyImport()`).
- Bewertung (•/••/••• im Kreis 0–3), Favorit ★ (erscheint in der Auswertung), Ursache/Warum-Ebene hinzufügen und löschen, Kategorie hinzufügen/löschen, Texteingabe mit HTML (escaped), Vorlage → automatische eigene Analyse (`autoAnlegen`).
- Rückgängig/Wiederholen, Verlauf-Dialog, Speichern + Autospeichern, Neuladen aus localStorage.
- Geführter Modus inkl. Kategorien-Vorlage im Assistenten, Reiter FAQ/Quiz/Wissensnetz, Quiz-Runde, Zoom/Vollbild/Anordnung zurücksetzen, Export-Knöpfe.

#### Auffällig, aber nicht geändert

- Kategorien-Vorlage verwirft (wie im Tooltip beschrieben) die Ursachen von Kategorien, deren Name im Schema nicht vorkommt (z. B. „Umfeld“, „Organisation“). Ohne Rückfrage – nur über Strg+Z zurückzuholen.
- Markdown-Import: eine eigene Kategorie mit „Favoriten“ oder „⭐“ im Namen wird als Favoritenliste übersprungen; mehrzeilige Ursachentexte (Umschalt+Enter) und leere Ursachen überstehen den Markdown-/Obsidian-Roundtrip nicht (JSON und HTML schon).
- Fußzeile „Speichern, Datensicherung & Datenschutz“ beschreibt veraltete Bedienelemente („Begehungen“, „HTML + Daten“, Strg+E) – nur Text.
- `wizSummary()` zählt „Unterursachen“ nur auf der ersten Warum-Ebene.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [ishikawa-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/ishikawa-v1.0.0) verfügbar.
