# Kanban-Regelkreisläufe – Änderungsprotokoll

*Kanban control loops – change log.* Phase 4 · Improve · Verbessern

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.2.2** | HTML-Download | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v2.2.2) |
| 2.2.1 | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v2.2.1) |
| 2.2.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v2.2.0) · [Live DE](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-regelkreislauf.html) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-control-loops.html) |
| 2.1.0 | English & Rüstzeit | 2026-10-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v2.1.0) |
| 2.0.0 | Pro | 2026-10-09 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v2.0.0) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.2.2 – HTML-Download (2026-10-13)

- Knopf „⬇ HTML“ in der Kopfleiste und auf der Startseite: das Tool als HTML-Datei herunterladen und offline nutzen

## 2.2.1 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.2.0 – Toolkit-Fassung (2026-10-12)

- Teil des Lean · CI · Kaizen Toolkits: Top-Leiste mit dem Verbesserungsprozess (Phase 4 · Improve), Vor/Zurück zum nächsten Tool, Link zur Übersicht
- Kopfbereich im Toolkit-Look mit animiertem Logo und 3D-Illustration (erstellt mit Codex)
- Neue Adresse: `tools/kanban-regelkreislauf.html` (DE) und `tools/kanban-control-loops.html` (EN); die alten Links leiten weiter
- Simulation, eigener PDF-Bericht und Datenformat unverändert

## 2.1.0 – English & Rüstzeit (2026-10-10)

- Vollständige englische Fassung (`kanban-control-loops.html`)
- Neuer Parameter **Rüstzeit** (Takte Linienstillstand je Variantenwechsel): Kunden entnehmen während des Stillstands weiter, kurze Lose plus lange Rüstzeit führen daher zu Fehlmengen; Optimieren berücksichtigt das
- Rüstzeit in Kennzahlen, Erzählung, Fabrik-Beschriftung, Markdown/JSON-Export und PDF-Bericht
- Gespeicherte Simulationen bleiben kompatibel (Standardwert 0 = bisherige Ergebnisse)

## 2.0.0 – Pro (2026-10-09)

#### Behobene Fehler gegenüber dem Original
- Palettengröße wählbar statt fest 4
- Die Linie läuft bei Lücken weiter (kein Stillstand mehr ohne Grund)
- Deadlock-Erkennung, wenn die Kanban-Anzahl kleiner als die Losgröße ist
- Das Fehlmengen-Urteil ist nur bei 0 Fehlmengen „grün“
- Die Sicherheitsgrenze skaliert mit dem Bedarf

#### Neu
- **✨ Optimieren:** kleinste Kanban-Anzahl mit 0 Fehlmengen (optional auch die Losgröße), mit Begründung, Rückgängig und „Ergebnis abspielen“
- Animierte Fabrik-Szene mit Illustrationen, Live-Erzählung und 7-Schritte-Ablaufleiste
- PDF-Bericht mit wählbaren Abschnitten
- Abschnitte per Drag & Drop, Mini-Player; die Seite bleibt beim Abspielen scrollbar

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [kanban-regelkreislauf-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kanban-regelkreislauf-v1.0.0) verfügbar.
