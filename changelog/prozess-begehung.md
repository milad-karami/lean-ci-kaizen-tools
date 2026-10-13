# Prozess-Begehung (Gemba) – Änderungsprotokoll

*Process walk-through (Gemba) – change log.* Phase 2 · Measure · Messen

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-begehung-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-begehung.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `prozess-begehung-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Nur das Anwendungsskript wurde geändert; eingebettete Bibliotheken (draw.io, bpmn-js, diagram-js, TipTap, Schriften) und die CSP-Meta-Angabe sind unverändert. Fixes sind mit `// FIX (Toolkit): …` markiert. IDs, localStorage-Schlüssel (`begehungW1T1.v2.*`), Datenformat und Exportstruktur unverändert.

Hinweis zum Smoke-Test: Es gibt kein `loadExample()`. Vorlagen und Begehungen werden über das Auswahlfeld `#exampleSel` geladen (`change` → `sofortSichern()` + `loadKey('ex:<id>' | 'p:<id>')`). Beim ersten Bearbeiten einer Vorlage legt das Tool automatisch eine Begehung an (`WB_CFG.autoAnlegen`).

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Nach einem Absturz wiederhergestellter Arbeitsstand ging verloren: Meldung „Letzter Arbeitsstand … wiederhergestellt“, aber der Stand galt als gespeichert, der Entwurf wurde gelöscht; beim Wechseln oder Schließen war er weg | `init()` ruft nach dem Laden aus dem Entwurf `clearDirty()` auf – der Entwurf wird gelöscht, die Begehung selbst behält den alten Inhalt | Kommt der Stand aus dem Entwurf und weicht er vom gespeicherten ab, wird er per `markDirty()` als ungesichert markiert (Autospeichern sichert ihn nach 3 s) | Zwei Läufe mit demselben Browserprofil: Begehung „Alt“ + neuerer Entwurf „Neu“ → nach dem Start ungesichert, nach 3 s ist „Neu“ in der Begehung gespeichert. Entwurf = gespeicherter Stand → nicht ungesichert |
| 2 | Strg+Z direkt nach „Berechnung/Begehung laden …“ (Import) schrieb den Inhalt der vorher offenen Begehung in die neu importierte | `applyImport()` stellt den Rückgängig-Verlauf nicht um (anders als `loadKey()`) | `WB.kontext()` nach dem Import | Vorher: nach Import + Strg+Z Firma = alter Wert. Jetzt: importierter Inhalt bleibt |
| 3 | Obsidian-Export erzeugt ungültigen YAML-Kopf, wenn Firmenname oder Datum `:` oder `#` enthält (z. B. „Müller & Co: Werk 2“) | Freitext unmaskiert in `unternehmen:` / `datum:` | Werte als JSON-String (gültiger YAML-Wert in Anführungszeichen) | `Müller & Co: Werk #2 "Nord"` wird korrekt zurückgelesen; Re-Import der Obsidian-Datei unverändert |

#### Getestet (headless Chrome, keine Konsolenfehler)

- Alle 3 Vorlagen über `#exampleSel` geladen; `buildMarkdown()`, `buildJSON()`, `buildObsidian()`, `WB.mdExport()` liefern Inhalt ohne NaN/undefined. Re-Import (Markdown, JSON, Obsidian, HTML mit eingebetteten Daten) ergibt für jede Vorlage exakt denselben Zustand, einschließlich Schaubild (Karte 04), Einschätzungshilfe und Schnittstellen.
- Felder bearbeiten (Stammdaten, Textfelder), Erledigt-Häkchen, Fragilitätsbewertung, Fortschritt und Bericht; automatische Anlage der Begehung, Autospeichern, Neuladen aus localStorage.
- Karte 04: Input anlegen, umbenennen (HTML wird escaped), verbinden, Querverbindung, löschen; Markdown-Zeilen korrekt. Einschätzungshilfe öffnen und beantworten.
- Geführter Modus (4 Schritte, Kartennavigation, Abschluss), Sprung aus dem Bericht, alle Reiter, alle nicht löschenden Knöpfe im Tool-Bereich angeklickt.

#### Auffällig, aber nicht geändert

- Der Markdown-Import sucht Abschnittsanker per erster exakter Zeile (z. B. `**Kultur**`, `**Input**`). Steht genau so eine Zeile als eigener Text in einem früheren Feld, wird falsch zugeordnet (selten; Exporte mit Datenkommentar sind ansonsten verlustfrei).
- Wiederhergestellte Begehungen aus dem Papierkorb behalten das Feld `deleted` (folgenlos).
- Ein Entwurf zu einer Vorlage (nur möglich, wenn das automatische Anlegen einer Begehung fehlschlug) wird durch Fix 1 ebenfalls als ungesichert markiert und bleibt als Entwurf erhalten, statt gelöscht zu werden.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [prozess-begehung-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-begehung-v1.0.0) verfügbar.
