# SMED-Rechner – Änderungsprotokoll

*SMED calculator – change log.* Phase 4 · Improve · Verbessern

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/smed-rechner-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/smed-rechner.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool
- Fehler behoben: Der Begriff „EPEI“ im FAQ zeigte die EKUV-Erklärung – jetzt eigener Glossar-Eintrag

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `smed-rechner-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`unit`, `procLabel`, `steps[]`), localStorage-Schlüssel (`smedW2T4.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | KPI-Kacheln zeigten immer „s“, auch bei Minuten-Beispielen (Presse, Spritzguss, Abfülllinie, Leer: „195→70 s“). Dezimalwerte erschienen ungerundet („0.30000000000000004“). | `renderKpis()` hatte `<small>s</small>` fest verdrahtet und gab die Rohzahlen aus. | `EINH()` für die Einheit und `zn()` für das deutsche Zahlenformat. | Alle 5 Beispiele: KPI zeigt „min“ bzw. „s“. Schritte 0.1 + 0.2 → „0,3→0,3 min“. |
| 2 | Markdown-Export: „Externe Rüstzeit (parallel) \| 0 s → 15 min“ bei Minuten-Beispielen. | „0 s“ war als Text fest eingetragen. | `zt(0)`. | Presse-Export: „0 min → 15 min“. |
| 3 | War die optimierte interne Zeit länger als die Ist-Zeit, stand dort „−-25 %“ (KPI, EKUV-Box, Markdown, Obsidian). | Das Minuszeichen war fest vor `red*100` gesetzt. | Kleiner Helfer `redTxt()` (− bei Einsparung, + bei Verschlechterung). | Leer-Vorlage, opt 15 statt 10 → „+25 %“. Normalfälle unverändert („−75 %“ bei Kaffee). |
| 4 | „Die drei Stufen“: Bei Minuten-Beispielen wurden die Balken mit festen 12 px je Einheit über 3.000 px breit (Spritzguss: Balken 3.346 px bei 1.234 px Container). Prozessblock und Summen lagen außerhalb des Sichtbereichs. | `SCALE=12` war konstant und unabhängig von der Größenordnung. | `SCALE` wird in `renderStages()` an die verfügbare Breite angepasst (max. 12, min. 1). Für Kaffee/Presse/Leer bleibt es bei 12 px, die Darstellung ist dort unverändert. | scrollWidth = clientWidth (1.234 px) für alle 5 Beispiele. Screenshot Spritzguss geprüft. |
| 5 | Wurde eine Datei mit ungültigen Daten importiert (z. B. JSON mit `_state` ohne `steps`), überschrieb das den Stand (`DATA=A.shape(s)\|\|s`), `renderAll()` brach ab und das Tool blieb kaputt. | Bei ungültigen Daten griff der Fallback auf die Rohdaten. | `applyImport()` wirft einen Fehler, bevor `DATA` überschrieben wird. Der bestehende Handler zeigt dann „Datei konnte nicht gelesen werden“. | Über den echten `#importFile`-Handler (DataTransfer) getestet: Meldung erscheint, der bisherige Stand bleibt erhalten. Vorher war `DATA` = `{"foo":1}`. |
| 6 | Enthielt ein Schrittname „-->“, ließen sich die eigenen Markdown- und Obsidian-Exporte nicht mehr importieren (JSON-Fehler „Unterminated string“). | `-->` im JSON beendete den `<!-- tool-state: … -->`-Kommentar vorzeitig. | `>` wird im State-Kommentar als `>` geschrieben (gültiges JSON, alte Exporte laden weiterhin). | Name `<b>x</b>\|a-->b` → Obsidian-Export → Import ergibt identischen Stand. |
| 7 | Ein „\|“ im Schrittnamen zerbrach die Markdown-/Obsidian-Tabelle. | Der Zellinhalt wurde nicht maskiert. | `mdCell()` maskiert `\|` als `\\|`. | Zeile: `\| <b>x</b>\\\|a-->b \| 1 \| vor …`. |

#### Was getestet wurde (headless Chrome, `cdp.mjs`)

- Laden ohne Konsolenfehler. Alle 5 Beispiele per `switchTo('ex:…')` geladen.
- Kennzahlen je Beispiel gegen Handrechnung geprüft, z. B. Kaffee: 32 → 9 (nach Verlagern) → 8 s intern, extern 23 → 17, gesamt 32 → 25, −75 %. Das entspricht dem Video.
- Eliminieren (opt = 0) und Umklassifizieren intern → extern verändern Stufe 2 und Stufe 3 korrekt.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel ohne NaN/undefined. Der Re-Import aller drei Formate ergibt jeweils exakt `DATA`.
- Schritte hinzufügen und löschen, Guide-Tabs 1–5, geführter Modus bis „fertig“ (Zusammenfassung), Tabs FAQ und Quiz.
- Speichern als Analyse → Store neu laden → `openKey` ergibt einen identischen Stand. Der Entwurf (`:draft`) wird nach dem Import geschrieben. `buildStandaloneHtml()` enthält den Stand.
- Escaping: HTML im Schrittnamen wird nicht als Markup gerendert.
- Shared `smoke.js`: keine Fehler.

#### Auffällig, aber nicht geändert

- Die Zeiteinheit (s/min) ist nur eine Beschriftung. Beim Umschalten werden die Werte nicht umgerechnet. Das ist vermutlich so gewollt.
- Die EKUV-Tabelle zeigt bei einer Verschlechterung (opt > Ist) als Ersparnis „0“ statt eines negativen Werts. Die Summe oben ist korrekt.
- Der Maßstab der Stufen wird nur beim Rendern berechnet, nicht bei einer Fenstergrößenänderung.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [smed-rechner-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/smed-rechner-v1.0.0) verfügbar.
