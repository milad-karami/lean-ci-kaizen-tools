# Five Forces – Änderungsprotokoll

*Five Forces – change log.* Phase 0 · Kontext & Strategie

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.0** | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/five-forces-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/five-forces-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/five-forces-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/five-forces.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/five-forces-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `five-forces-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`industry`, `forces{RIV,LIEF,ABN,NEU,SUB:{intensity,assess,drivers[{t,dir}]}}`), localStorage-Schlüssel (`fiveForcesW1T4.v1.*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Nach dem Wechsel der Vorlage über die Auswahlliste (mit „Trotzdem wechseln“) blieb der Stand als „noch nicht gespeichert“ markiert. Der alte Entwurf blieb im Speicher. Die verworfenen Änderungen kamen beim nächsten Öffnen zurück. | `loadKey()` rief nur `updateDirtyUI()` auf. `dirty` und `:draft` blieben erhalten. | `loadKey()` ruft bei nicht-stillem Laden `clearDirty()` auf. | Vorher: `dirty=true`, Draft mit `ex:tech`. Nachher: `dirty=false`, kein Draft, Status leer. |
| 2 | „Laden“ in der Analysen-Liste verwarf ungespeicherte Änderungen ohne Rückfrage. | Es gab keine `dirty`-Prüfung, anders als bei der Auswahlliste. | Die gleiche Rückfrage wie beim Wechsel über die Auswahlliste. | Mit `confirm=false` bleibt der Stand inklusive Änderung erhalten. |
| 3 | Ein wiederhergestellter Arbeitsstand (Entwurf nach Absturz/Schließen) galt sofort als gespeichert. `clearDirty()` löschte den Entwurf sogar. Beim nächsten Schließen gab es keine Warnung, die Arbeit war weg. | `init()` rief am Ende pauschal `clearDirty()` auf. | Kommt der Stand aus dem Entwurf und weicht er vom gespeicherten Stand bzw. von der Vorlage ab, wird anschließend `markDirty()` aufgerufen. Das Verhalten entspricht jetzt dem Speichermodul der anderen Tools. | Neuladen (iframe): vorher `dirty=false`, Status leer. Nachher `dirty=true`, „noch nicht gespeichert“, Entwurf bleibt. Neuladen ohne Entwurf bleibt sauber. |
| 4 | Nach „Speichern“ (neue Analyse) oder Import öffnete das Tool beim nächsten Start wieder die Vorlage statt der Analyse. | `K_LAST` (zuletzt aktiv) wurde nur in `loadKey()`/`loadExample()` gesetzt, nicht in `doSaveAs()` und `applyImport()`. | `safeSet(K_LAST, curKey)` an beiden Stellen. | Speichern → Neuladen: `curKey` = gespeicherte Analyse (vorher `ex:tech`). |
| 5 | Eine mehrzeilige Begründung ging beim Re-Import von Markdown/Obsidian ab der 2. Zeile verloren. | Export: nur die erste Zeile mit `> `. Import: liest nur eine Zitatzeile. | Export setzt `> ` vor jede Zeile. Der Import hängt folgende `>`-Zeilen an. | „Zeile 1\n\nZeile 3\n“ → Markdown und Obsidian → Import identisch. |
| 6 | Treiber ohne Text (`- ↑`) wurden beim Import verworfen, dadurch änderte sich die Treiber-Bilanz. | Die Regex verlangte Leerraum und Text nach dem Symbol. | Der Text nach dem Symbol ist optional. | 4 statt 3 Treiber nach dem Re-Import. Die Beispiele importieren weiter identisch. |
| 7 | Obsidian-Mindmap: Die Knoten der Kräfte zeigten nur „hoch“/„mittel“/„niedrig“, der Name der Kraft fehlte. | `Name [hoch]` ist in Mermaid-Mindmaps die Syntax `id[Text]` (eckiger Knoten mit Text „hoch“). | `Name · hoch`. | Ausgabe: „Rivalität in der Branche · hoch“ usw. |

#### Was getestet wurde (headless Chrome, `cdp.mjs`)

- Laden ohne Konsolenfehler. Alle 5 Vorlagen, Leitfaden-Schritte 1–5.
- Bilanzvorschläge und Stärken aller Vorlagen nachgerechnet (⅔/⅓-Regel). Zonen 5–8 / 9–11 / 12–15 Punkte passen zu den Grenzen 1,7 / 2,3 und zu den Gauge-Ticks.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jede Vorlage ohne NaN/undefined. Der Re-Import aller drei Formate ergibt jeweils dieselben Kräfte und dieselbe Branche.
- Geführter Modus: alle Kräfte einzeln (vorherige/nächste Kraft), Gesamtbild, SWOT-Übergabe, „fertig“. FAQ-Tab.
- Speichern, Autosave, Neuladen, Entwurf, Projektliste (Löschen/Papierkorb/Wiederherstellen). Schmale Ansicht (iframe 375 px): kein horizontales Überlaufen.

#### Auffällig, aber nicht geändert

- Die Übergabe an die SWOT ist manuell (Export als Vorlage). Die SWOT-Analyse kann eine Five-Forces-Datei nicht importieren, aus einem Obsidian-Export übernimmt sie nur die Branche als Betrachtungsobjekt. Der FAQ-Satz „Genau diese Übergabe an die SWOT ist eingebaut“ meint die angezeigte Brücke (Bedrohungen/Chancen).
- Das Beispiel „Apfel-Marke“ in der SWOT führt die schwache Lieferantenmacht als Stärke (S), nicht als Chance (O). Das ist eine inhaltliche Frage, kein Code-Fehler.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [five-forces-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/five-forces-v1.0.0) verfügbar.
