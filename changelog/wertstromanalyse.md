# Wertstromanalyse (IST & SOLL) – Änderungsprotokoll

*Value stream mapping (current & future) – change log.* Phase 3 · Analyze · Analysieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.3** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v2.1.3) |
| 2.1.2 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/wertstromanalyse-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/wertstromanalyse.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.3 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool
- Fehler behoben: Die Rechnung zum Kundentakt sprang ohne Umrechnung von Minuten zu Sekunden – jetzt „min × 60 s ÷ Stück“

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `wertstromanalyse-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes sind im Code mit `// FIX (Toolkit): …` markiert. IDs, localStorage-Schlüssel (`wertstromW2T3.v1:*`), Datenformat der Projekte und Exportstruktur unverändert. Oberfläche weiterhin Deutsch, Credits (John Naska, mokka.solutions; Videoquellen) unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | „Offene Probleme“ und Balancing-Diagramm bleiben veraltet, wenn in Schritt 1 Bedarf, Schichten, Pause oder Varianten geändert werden (z. B. Aufgabe 1: Bedarf 100 → 1000, Takt 270 → 27 Sek – Liste zeigt weiter „Losgröße 200 vs. 100 Stk/Tag“ und keinen Engpass) | Die Eingabe-Handler für Stammdaten (`data-pm`, `data-vd`) und `afterVariants()` rufen `renderProblems()` nicht auf; bei `data-pm` fehlte auch `renderOverview()` (Takt-Flags der Übersicht) | `renderProblems()` (und `renderOverview()`) in diesen Handlern ergänzt | Bedarf geändert → Problemliste = `buildProblems()` (enthält jetzt „Zykluszeit über Kundentakt“) |
| 2 | Nach Einfügen, Löschen oder Umsortieren (Drag-and-drop) von Prozessen/Beständen zeigt das Balancing die gestrichelten Ausgangswerte an den falschen Stationen; ein eingefrorenes Szenario setzt die Zykluszeiten bei den falschen Prozessen | `_base` und Szenario-Werte (`_scen[].vals`) sind nach Knoten-Index abgelegt, die Indizes verschieben sich | Neue Hilfsfunktion `remapIdx()` schlüsselt beide Maps bei `addNode`, `delNode` und `commitOrder` auf die neuen Indizes um | Stanz AG SOLL, ersten Bestand gelöscht: Basis je Station = eigener Wert (vorher Schweißen 2 ↔ 39 usw.); Szenario nach Löschen/Einfügen/Umsortieren angewendet → richtige Werte an richtigen Prozessen |
| 3 | Import einer ungültigen Datei (gültiges JSON mit `_state`, aber ohne IST/SOLL) zerstört den aktuellen Stand – danach wirft jedes Neuzeichnen einen Fehler | `applyImport()` übernahm bei `A.shape()===null` die Rohdaten (`DATA=A.shape(s)||s`) | Ungültige Daten (ohne `ist`/`soll` mit `pps`, `customer`, `supplier`) werfen einen Fehler, der aktuelle Stand bleibt; Meldung „Datei konnte nicht gelesen werden“ | `applyImport({_x:1})` → Fehler, `DATA` unverändert, `renderKpis()` läuft |
| 4 | Fehlendes Escaping: Variantenname erscheint ungefiltert in der Prozessdaten-Übersicht; Zahlenfelder (`shifts`, `workers`, `packSize`, …) und die Übergangsart (`link`) aus importierten Dateien landen unescaped in HTML/SVG/Attributen | `renderOverview()` ohne `esc()`; Importe werden nur strukturell geprüft, Zahlen nicht typisiert | `esc()` für den Variantennamen; `normalizeData()` (läuft bei jedem Laden/Import) wandelt Zahlenfelder, Mengen, Parameter und Bedarfe in Zahlen und setzt unbekannte `link`-Werte auf `auto` | Variantenname `<b id="xss">` und importierte Felder `shifts`/`link` mit HTML: kein eingeschleustes Element mehr |
| 5 | Eingefrorene Szenarien („❄ Einfrieren“) gehen nach Speichern + erneutem Öffnen verloren und lösen keine Speicher-Markierung aus | `A.shape()` (Laden) und `A.cmp()` (Änderungserkennung) verwerfen alle Schlüssel mit `_`, auch `_scen` (Nutzerinhalt) | `_scen` wird in `A.shape()` und `A.cmp()` durchgelassen (gespeicherte Daten enthielten `_scen` bereits – kein neues Format) | Szenario angelegt, gespeichert, andere Vorlage geöffnet, Analyse wieder geöffnet → Szenario vorhanden; ebenso nach Entwurf-Wiederherstellung |
| 6 | Import einer Markdown-/Obsidian-Datei scheitert, sobald ein Name `-->` enthält | Zustand steht als JSON in `<!-- tool-state: … -->`, `-->` beendet den Kommentar | `stateComment()` maskiert `>` als `>` (gleiches Vorgehen wie in oee-rechner) | Prozessname `Stanzen --> "x" <b>` → MD und Obsidian re-importiert, Name identisch |

#### Getestet (headless Chrome, keine Konsolenfehler)

- Alle 5 Vorlagen (Stanz AG, Pumpenwerk, Bäckerei, Aufgabe 1, Leer), IST und SOLL, alle Schritte 1–5 des Aufbaus und alle 7 Fragen: kein NaN/undefined in der Oberfläche.
- Rechenwerte geprüft: Kundentakt = Schichten × (Schichtdauer − Pause) × 60 / Gesamtbedarf (Stanz 60 s, Pumpe 115 s, Bäckerei 23 s, Aufgabe 1 270 s, Leer 112,5 s); Reichweite Mengenbestand = Σ Menge / Gesamtbedarf; Liegezeit = Σ Reichweiten (Stanz IST 23,6 Tage, SOLL 7 Tage; Aufgabe 1 IST 8 / SOLL 2 Tage); Bearbeitungszeit = Σ ZZ (188 s / 105 s); DLZ = Liegezeit + BZ/Betriebszeit; Flussgrad = BZ / DLZ (beides auf Arbeitszeit-Basis, konsistent); ZZ > Takt-Markierung; Kapazitäts-Check = Betriebszeit / ZZ × MZ.
- `buildMarkdown()`, `buildJSON()`, `buildObsidian()` je Vorlage; Re-Import aller Exporte ergibt denselben Zustand.
- Drag-and-drop-Umsortierung (`commitOrder`), Prozess/Bestand/Supermarkt hinzufügen/löschen, Einheit Tage ↔ Stück, Zellen, Übergang Push/Pull, Varianten hinzufügen/löschen, Push/Pull-Umschaltung, Pitch automatisch/leeren, SOLL aus IST übernehmen/rückgängig.
- Konsistenz-Checks und Problemkarten anklicken (Sprung + Hinweis), geführter Modus komplett, Reiter FAQ/Legende/Quiz, Quiz-Runde, Datei-Menü.
- Speichern als Analyse, Laden, Projektliste, Autospeichern nach 3 s, Entwurf-Wiederherstellung nach „Absturz“ (`bootStore`), eingebettete HTML-Kopie.

#### Auffällig, aber nicht geändert

- Exporte schreiben unter „Offene Probleme & Lösungen“ / `offene_probleme` / `linienbalancing` die **festen Musterlösungen der Vorlage** (`DATA.problems`, `DATA.balancing`), nicht die live berechneten Probleme der Oberfläche. Bei eigenen Analysen (Basis „Leer“) fehlt der Abschnitt, bei geänderten Werten passt er nicht mehr zu den Daten. Nicht geändert, weil die Musterlösungen je Vorlage unterschiedlich gemeint sind (Aufgabe 1 beschreibt die IST-Probleme als Lösung der Kursaufgabe).
- Export-Titel verwendet immer den Namen der Basis-Vorlage (`EXAMPLES[curId].label`), nicht den Namen der gespeicherten Analyse.
- Kapazitäts-Check rechnet mit den Schichten aus Schritt 1, nicht mit den Schichten des einzelnen Prozesses (Datenkasten); in den Vorlagen ohne Auswirkung auf das Ergebnis.
- Flussgrad bezieht sich auf Arbeitstage (Betriebszeit), nicht auf Kalenderzeit – Stanz IST 0,014 % statt ca. 0,009 % bei 24-h-Tagen. Konsistent mit „Reichweite in Tagen Kundenbedarf“, daher belassen.
- Symbol-Legende (iframe): einige Erklärtexte haben vertauschte Anführungszeichen (z. B. `'I"`, `'geschoben"`) – reiner Text, nicht geändert.
- `loadExample(id)` (nur Test-Hilfsfunktion, in der Oberfläche nicht verwendet) setzt das Auswahlfeld auf einen nicht existierenden Wert (`stanz` statt `ex:stanz`) und aktualisiert `curKey` nicht.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [wertstromanalyse-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/wertstromanalyse-v1.0.0) verfügbar.
