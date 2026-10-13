# Heijunka – Änderungsprotokoll

*Heijunka – change log.* Phase 4 · Improve · Verbessern

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.0** | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/heijunka-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/heijunka-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/heijunka-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/heijunka.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/heijunka-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `heijunka-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`DATA`: `variants[]`, `hoursPerDay`, `daysPerWeek`, `weeksPerMonth`, `phase`, `manualBasic`), localStorage-Schlüssel (`heijunkaW2T3.v1:*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

#### Behobene Fehler

##### 1. Basiswoche rundete Varianten ohne Rest bzw. mit Bedarf 0 auf (Überproduktion)
- **Fehler:** `computeWeeklyBasic()` verteilte die freien Slots der Basiswoche an die „größten Reste“, rankte aber **alle** Varianten – auch solche mit Rest 0 und Bedarf 0. Bei Unterauslastung (z. B. Beispiel „Einfach · 3 Typen“: 140 h Bedarf, 160 h Kapazität) bekam jede Variante „+1“: Basiswoche 21/11/6 statt 20/10/5, Ausgleichswoche 17/7/2. Eine per „+ Variante“ angelegte Variante (Bedarf 0) wurde 3× pro Monat gefertigt, Kontrolle zeigte „warn“. Kleine Bedarfe (1–2 Stück) konnten so weit aufgerundet werden, dass (Wochen−1)×Basis den Monatsbedarf überstieg.
- **Ursache:** Kein Filter auf `frac>0`, keine Begrenzung gegen den Monatsbedarf.
- **Fix:** Nur Varianten mit echtem Nachkommarest aufrunden, zuerst nur solange (Wochen−1)×(Basis+1) ≤ Monatsbedarf. Nur wenn die Ausgleichswoche sonst überliefe (Stücke gingen still verloren), wird wie bisher weiter aufgerundet.
- **Geprüft:** Beispiele Video und Hochmix unverändert (7,15,5,5,2,1 / 10,8,6,4,3,2,1,1). Einfach jetzt 20/10/5, Ausgleich 20/10/5, Monatssummen = Bedarf. Einfach + „+ Variante“: neue Variante 0 Stück, keine „warn“ (vorher 3 Stück, 1 warn). Brute-Force über 2.861 Zufallskonfigurationen mit Bedarf ≤ Kapazität: Monatsplan ≠ Monatsbedarf sinkt von 1.046 auf 115 Fälle. Die übrigen Fälle sind strukturell unlösbar (Kapazität zu klein für „gleiche Basiswochen + 1 Ausgleichswoche“).

##### 2. Import einer fremden/ungültigen Datei machte das Tool unbenutzbar
- **Fehler:** `applyImport()` setzte `DATA=A.shape(s)||s`. Hatte die Datei einen `tool-state` ohne `variants` (z. B. Export eines anderen Tools), wurde das Rohobjekt zum Zustand; `derive()` stürzte ab (`Cannot read properties of undefined (reading 'reduce')`), jedes weitere Rendern ebenfalls.
- **Fix:** Liefert `A.shape()` `null`, wird ein Fehler geworfen; der vorhandene catch zeigt „⚠ Datei konnte nicht gelesen werden“, der aktuelle Stand bleibt.
- **Geprüft:** Fremde Datei abgelehnt, `DATA` unverändert, `renderAll()` läuft. Gültiger `.md`-Export wird weiterhin importiert.

#### Ohne Befund geprüft
Alle 4 Beispiele über das Auswahlfeld; Schritt-Tabs 1–6; `buildMarkdown/buildJSON/buildObsidian` je Beispiel; Import-Rundlauf (MD + JSON) ergibt identischen Stand; kein NaN/undefined in der Oberfläche; Parameter-Eingaben, Phasen-Knöpfe 0/0,5/1, manuelles Umsortieren per Drag & Drop (`applyManualMove`) inkl. Zurücksetzen bei Parameteränderung; Speichern als Projekt → Neuladen aus localStorage → Stand inkl. manueller Reihenfolge wiederhergestellt; Entwurf wird geschrieben; Geführter Modus bis „fertig“; FAQ-/Quiz-Reiter. Keine Konsolenfehler.

#### Aufgefallen, nicht geändert
- „+ Variante“ in Beispielen mit weniger als 6 Varianten vergibt Namen, die nicht zur Farbe passen (z. B. „Violett“ in Orange), weil Namens- und Farbindex unabhängig sind. Nur kosmetisch.
- Bei 1 Woche/Monat zeigen Überschriften „×0“ / „Basiswoche (1…0)“. Nur kosmetisch.
- Variantennamen mit `|` brechen die Markdown-Tabellenzeilen.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [heijunka-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/heijunka-v1.0.0) verfügbar.
