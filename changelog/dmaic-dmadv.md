# DMAIC & DMADV – Änderungsprotokoll

*DMAIC & DMADV – change log.* Phase 1 · Define · Definieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.4** | Illustration | 2026-10-14 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/dmaic-dmadv-v2.1.4) |
| 2.1.3 | Toolkit-Fassung | 2026-10-14 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/dmaic-dmadv-v2.1.3) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/dmaic-dmadv.html) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/dmaic-dmadv-en.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/dmaic-dmadv-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.4 – Illustration (2026-10-14)

- Eigene 3D-Illustration (erstellt mit Codex) im Kopfbereich, auf der Startseite und im README – statt des Platzhalters

## 2.1.3 – Toolkit-Fassung (2026-10-14)

Neu im Toolkit (Kurs Woche 3, Tag 2). Das Tool steigt direkt auf dem Stand der übrigen Tools ein, deshalb Version 2.1.3. Es steht in Phase 1 (Define) vor SIPOC, weil es den ganzen Verbesserungsweg erklärt.

#### Neu gegenüber dem Original
- Gemeinsame Toolkit-Ebene: Top-Leiste mit dem Verbesserungsprozess, Kopfzeile mit LinkedIn-Link und Hinweis auf das Original-Tool, **📄 Bericht (PDF)**, **⬇ HTML**-Download, Versionsnummer und Link auf dieses Änderungsprotokoll
- Vollständige englische Fassung `dmaic-dmadv-en.html`: Oberfläche, Fallbeispiele, Tollgates, Glossar, geführter Modus, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; gespeicherte Projektplanungen werden zwischen beiden Sprachen geteilt
- Werkzeug-Code, Datenformat, Speicherschlüssel (`dmaicDmadvW3T2.v1:*`) und Exportstruktur bleiben kompatibel zum Original

#### Behobene Fehler

Fixes sind im Code mit `// FIX (Toolkit): …` markiert.

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Import einer Markdown-/Obsidian-Datei scheiterte, sobald ein Text `-->` enthielt (z. B. Szenario „A --> B“) | Zustand steht als JSON in `<!-- tool-state: … -->`; `-->` beendet den Kommentar | `stateComment()` maskiert `>` als `\u003e` | Original: `SyntaxError` beim Re-Import; jetzt identischer Zustand |
| 2 | Ungültige Datei meldete „✓ … geladen“ und schaltete auf „Import (ungespeichert)“, obwohl nichts übernommen wurde | `applyImport()` prüfte das Ergebnis von `A.shape()` nicht | Fehler vor jeder Änderung; Meldung „Datei konnte nicht gelesen werden“ | Ungültige Daten: keine Erfolgsmeldung, Stand unverändert |
| 3 | Projekt-Kennzahl: Baseline und Ziel wurden beim ersten Zeichnen unmaskiert ins HTML geschrieben – HTML/Skript aus einer importierten Datei wurde ausgeführt | Fehlendes `esc()` in `renderKpi()` (die Live-Aktualisierung maskierte bereits) | Werte maskiert | Baseline `4<img onerror=…>`: Original führt den Code aus, jetzt nicht |
| 4 | Obsidian-Export: Kopfzeile `fallbeispiel:` wurde ungültiges YAML, wenn der Name `:` enthielt | Freitext unmaskiert im YAML-Kopf | Wert als JSON-String | Name mit Doppelpunkt wird korrekt gelesen |

#### Getestet (headless Chromium, keine Konsolenfehler, DE und EN)

- Alle 5 Fallbeispiele × DMAIC/DMADV × 5 Phasen gerendert; `buildMarkdown()`, `buildJSON()`, `buildObsidian()` ohne NaN/undefined; Re-Import aus allen drei Formaten ergibt denselben Zustand
- Alle Knöpfe im Tool-Bereich (außer Löschen) angeklickt, Reiter, geführter Modus, FAQ, Quiz

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs (Woche 3, Tag 2), so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [dmaic-dmadv-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/dmaic-dmadv-v1.0.0) verfügbar.
