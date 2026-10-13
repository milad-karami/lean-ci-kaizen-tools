# Prozess-Analyse (Toyota Kata) – Änderungsprotokoll

*Process analysis (Toyota Kata) – change log.* Phase 2 · Measure · Messen

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.2** | Toolkit-Fassung | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-analyse-v2.1.2) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-analyse.html) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-analyse-en.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-analyse-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.2 – Toolkit-Fassung (2026-10-13)

Neu im Toolkit (Kurs Woche 3, Tag 1). Das Tool steigt direkt auf dem Stand der übrigen Tools ein, deshalb Version 2.1.2.

#### Neu gegenüber dem Original
- Gemeinsame Toolkit-Ebene: Top-Leiste mit dem Verbesserungsprozess (Phase 2 · Measure, nach dem OEE-Rechner), Kopfzeile mit LinkedIn-Link und Hinweis auf das Original-Tool, **📄 Bericht (PDF)**, Versionsnummer und Link auf dieses Änderungsprotokoll
- Vollständige englische Fassung `prozess-analyse-en.html`: Oberfläche, Beispiele, Glossar, geführter Modus, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; gespeicherte Analysen werden zwischen beiden Sprachen geteilt
- Werkzeug-Code, Datenformat, Speicherschlüssel (`prozessAnalyseW3T1.v1:*`) und Exportstruktur bleiben kompatibel zum Original

#### Behobene Fehler

Fixes sind im Code mit `// FIX (Toolkit): …` markiert.

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Zahlen in den Tabellen „Ausbringung“ und „Ausgabezyklen“ änderten nur die Kurve: Storyboard (Diagramme, T-Formular „Output in Stück“), Kennzahlen, Spaltensumme und Min/Ø/Max blieben veraltet, bis an anderer Stelle etwas geändert wurde | Der Eingabe-Handler der Tabellen zeichnet nur das Diagramm neu | Während der Eingabe Storyboard und Kennzahlen nachführen, beim Verlassen des Felds alles neu zeichnen | Montag Woche 1 auf 5 Stk: Storyboard ändert sich sofort, Plan-Summe danach −8.825; Zyklus 1 auf 99 s: Max 99 s, Spreizung 76 s |
| 2 | Import einer Markdown-/Obsidian-Datei scheiterte („Datei konnte nicht gelesen werden“), sobald ein Text `-->` enthielt (z. B. Beobachtung „A --> B“) | Zustand steht als JSON in `<!-- tool-state: … -->`; `-->` beendet den Kommentar | `stateComment()` maskiert `>` als `\u003e` (wie in den übrigen Tools) | Original: `SyntaxError` beim Re-Import; jetzt identischer Zustand nach Re-Import aus Markdown und Obsidian |
| 3 | Import einer ungültigen Datei (z. B. JSON mit `_state`, aber ohne Objekt) überschrieb den Stand und ließ das Tool kaputt zurück | `applyImport()` übernahm bei `A.shape()===null` die Rohdaten (`P=A.shape(s)\|\|s`) | Fehler vor dem Überschreiben; Meldung „Datei konnte nicht gelesen werden“ | Ungültige Daten: Stand bleibt unverändert |
| 4 | `\|` in einem Anlagennamen zerbrach die Markdown-Tabelle „Anlagenkapazität“ | Name unmaskiert in der Tabellenzelle | Maskierung `\|` | „Schweiß\|anlage“ steht korrekt in einer Zelle |
| 5 | Negative Takt- und Zykluszeiten, wenn Pause bzw. Verluste größer sind als die Arbeitszeit (z. B. Verluste 5000 min → geplante Zykluszeit −133 s) | Keine Untergrenze in `calc()` | Verfügbare und nutzbare Zeit nicht unter 0 | Verluste 5000 min: geplante Zykluszeit 0 s, keine negativen Werte |
| 6 | Kennzahl „Gesamt-Arbeitsinhalt“ zeigte immer „MA 1–3 summiert“, auch bei 2 oder 4 Mitarbeitern | Fester Text | Anzahl aus den Eingaben | 4 Mitarbeiter: „MA 1–4 summiert“ |
| 7 | Urteil zur Anlagenkapazität nannte immer „Engpass beim Schweißen“, auch wenn eine andere Anlage (oder mehrere) über der geplanten Zykluszeit lag | Fester Text aus dem Video-Szenario | Allgemein „Engpass erkannt“, Verb passt zur Anzahl der Anlagen | Fallbeispiel „Engpass“ und eigene Anlagen |

#### Getestet (headless Chromium, keine Konsolenfehler, DE und EN)

- Alle 4 Vorlagen geladen; `buildMarkdown()`, `buildJSON()`, `buildObsidian()` ohne NaN/undefined; Re-Import aus allen drei Formaten ergibt denselben Zustand
- Randwerte: keine Anlagen, Bedarf 0, Schichten 0, Verluste > Arbeitszeit, Mitarbeiter mit 0 s, sehr große Ausbringung, halbe Schichten – keine Fehler, keine NaN/Infinity in Oberfläche, Diagrammen und Exporten
- Alle Knöpfe im Tool-Bereich (außer Löschen) angeklickt, Reiter, geführter Modus, FAQ, Quiz

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs (Woche 3, Tag 1), so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [prozess-analyse-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/prozess-analyse-v1.0.0) verfügbar.
