# Kano-Modell – Änderungsprotokoll

*Kano model – change log.* Phase 1 · Define · Definieren

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.0.0** | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kano-modell-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kano-modell.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kano-modell-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.0.0 – Toolkit-Fassung (2026-10-12)

#### Neu in allen Tools (gemeinsame Toolkit-Ebene)
- Einheitliches Design: dunkler Kopfbereich, animiertes Toolkit-Logo, 3D-Illustration (erstellt mit Codex)
- Top-Leiste mit dem Verbesserungsprozess (0 Kontext → 5 Control), aktuelle Phase markiert, Vor/Zurück zum nächsten Tool
- **📄 Bericht (PDF)**: professioneller A4-Bericht mit Deckblatt, Inhaltsverzeichnis, Glossar und Quellen; Abschnitte per Häkchen wählbar
- Hinweis auf diese Fassung, Versionsnummer und Link auf dieses Änderungsprotokoll im Fußbereich
- Werkzeug-Code, Datenformat, Speicherschlüssel und Exporte bleiben kompatibel zum Original

#### Fehlerkorrekturen gegenüber dem Original

#### Behobene Fehler

| # | Fehler | Ursache | Fix | Verifiziert |
|---|---|---|---|---|
| 1 | Beim Import einer exportierten Markdown-/Obsidian-Datei gehen die einzelnen Antworten verloren (nur grobe Verteilung bzw. Platzhalter-Antworten), wenn ein Merkmal oder das Produkt `-->` enthält. | `stateComment()` schreibt `kano-data` als JSON in einen HTML-Kommentar; `-->` beendet ihn vorzeitig, `JSON.parse` scheitert und der Import fällt auf die verlustbehaftete Text-Auswertung zurück. | `>` im JSON als `>` maskieren (gültiges JSON, Format unverändert). | Headless Chrome: Merkmal „a --> b" → Rückimport aus MD und Obsidian identisch (vorher abweichend). |

#### Geprüft ohne Befund
- Schrittnavigation: Das Tool hat kein `showStep()`, sondern eigene Navigation (`state.step` + Stepper `[data-go]`, Schrittnummern unten, Weiter/Zurück, „✓ fertig" → Abschlussbox). Alle 5 Schritte für alle 5 Vorlagen durchlaufen – funktioniert.
- Kano-Auswertung: `collate()`/`winner()` liefern die erwarteten Kategorien für alle Beispiele (Hotel M P P D I R, Video D P M M I, App M P D D R I, Shop M P D R I); Gleichstand-Regel M > P > D > R > I > Q.
- Schritt 1/2/3: Merkmale hinzufügen/löschen/umbenennen, Befragte hinzufügen/wechseln/entfernen, Antwortzellen klicken (Live-Kategorie + Lesart), Zellenhervorhebung in der Auswertungstabelle.
- `buildMarkdown()`, `buildJSON()`, `buildObsidian()` je Vorlage; Rückimport aller drei Formate identisch. Mermaid-Bereinigung (Klammern, Anführungszeichen) ok.
- Speichern als Analyse, Neuladen aus localStorage. HTML-Escaping aller Nutzertexte (kein Script ausgeführt).
- Legende/Diagramm, FAQ, Quiz (74 Fragen strukturell geprüft, komplette Runde). Keine Konsolenfehler.
- Better/Worse-Koeffizienten werden im Tool nicht berechnet; nur eine Quizfrage nennt die Formel (A+O)/(A+O+M+I) – korrekt.

#### Auffällig, nicht geändert
- Auswertungstabelle (`KANO`): Die Felder „Erwarte ich/Erwarte ich" und „Tolerierbar/Tolerierbar" sind als **Q** (fragwürdig) hinterlegt; die klassische Tabelle (Berger et al. 1993) hat dort **I**. Laut Code-Kommentar „exakt nach Vorlage" (Video) und das Quiz klammert genau diese zwei Felder bewusst aus – daher belassen. Fachlich zu entscheiden.
- Die Antwortzellen in Schritt 2 sind `div`s mit Klick-Handler – per Tastatur nicht bedienbar (Barrierefreiheit). Nicht geändert, weil dafür Markup und Styling angepasst werden müssten.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [kano-modell-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/kano-modell-v1.0.0) verfügbar.
