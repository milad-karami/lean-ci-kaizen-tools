# OEE-Rechner – Änderungsprotokoll

*OEE calculator – change log.* Phase 2 · Measure · Messen

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.1** | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/oee-rechner-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/oee-rechner-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/oee-rechner-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/oee-rechner-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/oee-rechner.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/oee-rechner-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `oee-rechner-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes sind im Code mit `// FIX (Toolkit): …` markiert. IDs, localStorage-Schlüssel (`oeeW2T4.v1:*`), Datenformat und Exportstruktur unverändert.

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Import einer Markdown-/Obsidian-Datei scheitert („Datei konnte nicht gelesen werden“), sobald eine Verlust-Bezeichnung `-->` enthält | Der Zustand steht als JSON in `<!-- tool-state: … -->`; ein `-->` im Text beendet den Kommentar vorzeitig, `JSON.parse` bricht ab | `stateComment()` maskiert `>` im JSON als `>` (wird von `JSON.parse` wieder zu `>`) | Bezeichnung `Störung --> "x" <b>` → `buildMarkdown()`/`buildObsidian()` → `importFromText()` ergibt identischen Zustand (vorher: „Unterminated string in JSON“) |
| 2 | Berechnung ändert sich nach Speichern + Neuladen, wenn GPS > „Tag gesamt“ eingegeben ist (z. B. Tag 10 h, GPS 16 h: OEE 65,6 % → nach Neuladen 45,0 %) | Eingabe begrenzt GPS nur auf 24 h, der Lade-Validator `A.shape()` kürzte GPS aber still auf „Tag gesamt“ | `A.shape()` begrenzt GPS wie die Eingabe auf 24 h | Projekt mit Tag 10 h / GPS 16 h gespeichert, Projekte neu aus localStorage geladen: GPS 16 h, OEE unverändert |
| 3 | Zeitkaskade läuft über 100 % hinaus (Balken 160 %, bei „Tag gesamt“ = 0 sogar 96 000 %) | Breitenbezug war nur „Tag gesamt“ (`c.dayMin||1`) | Bezugsbreite = max(Tag gesamt, GPS) | Tag 10 h/GPS 16 h und Tag 0: alle Balken ≤ 100 % |

#### Getestet (headless Chrome, keine Konsolenfehler)

- Alle 5 Vorlagen: OEE = Musterlösung (65,6 % · 66,8 % · 68,8 % · 94,0 % · 100 %); V = verfügbar/GPS, L = genutzt/verfügbar (= ideale Zykluszeit × Menge / Laufzeit im Mengen-Modus), Q = Gut/produziert, OEE = V×L×Q.
- `buildMarkdown()`, `buildJSON()`, `buildObsidian()` für jede Vorlage: Inhalt vorhanden, kein NaN/undefined; Re-Import aller drei Formate liefert dieselben Werte.
- Einheitenwechsel h ↔ min (Anzeige und Eingabe in min korrekt umgerechnet), Verluste hinzufügen/löschen, Modus „Produzierte Menge“ ↔ „Verluste in min“ (Hin- und Rückweg verlustfrei), Menge > Maximum (Warnung, Rechnung mit Maximum), Ausschuss > Produktion (Q = 0), Idealrate 0 (→ 0,01), Tag/GPS = 0: kein NaN/Infinity in der Oberfläche.
- HTML in Bezeichnungen wird escaped (kein eingeschleustes Element).
- Speichern als Berechnung, Neuladen aus localStorage, geführter Modus (alle 7 Schritte + Abschluss), Schrittreiter, FAQ-/Quiz-Reiter, Quiz-Runde durchgespielt.

#### Auffällig, aber nicht geändert

- Nach einem Import bleibt die zuvor gewählte Vorlage für die „Schritt für Schritt“-Tabelle aktiv; die Live-Kontrolle zeigt dann ggf. „weicht von der Musterlösung ab“ (Exportdatei speichert keine Vorlagen-ID).
- Entwurf-Wiederherstellung vergleicht per `JSON.stringify` mit abweichender Schlüsselreihenfolge (KaffeKönig/Werkstatt): ein unveränderter Entwurf kann als „ungespeichert“ gelten. Nur kosmetisch.
- „Größter Hebel“ in der Verlust-Analyse zeigt immer Stunden, auch im Minuten-Modus.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [oee-rechner-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/oee-rechner-v1.0.0) verfügbar.
