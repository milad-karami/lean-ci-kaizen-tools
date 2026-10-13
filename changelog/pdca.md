# PDCA-Zyklus – Änderungsprotokoll

*PDCA cycle – change log.* Phase 5 · Control · Sichern

| Version | Name | Datum | Download |
|---|---|---|---|
| **2.1.2** | Sprachwechsel | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v2.1.2) |
| 2.1.1 | Einheitlicher Kopf | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v2.1.1) |
| 2.1.0 | English | 2026-10-13 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v2.1.0) · [Live EN](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/pdca-en.html) |
| 2.0.0 | Toolkit-Fassung | 2026-10-12 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v2.0.0) · [Live](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/pdca.html) |
| 1.0.0 | Original (John Naska) | 2026-10 | [Release](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v1.0.0) |

Original-Tool: John Naska ([mokka.solutions](https://www.mokka.solutions/)), veröffentlicht mit seiner Genehmigung.
Weiterentwicklung: [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/).

## 2.1.2 – Sprachwechsel (2026-10-13)

- Beim Sprachwechsel bleiben Reiter und Scrollposition erhalten; die Daten werden ohnehin geteilt

## 2.1.1 – Einheitlicher Kopf (2026-10-13)

- Kopfzeile wie im Kanban-Tool: Entwicklung mit LinkedIn-Link, Sprachwechsel, Hinweis auf das Original-Tool

## 2.1.0 – English (2026-10-13)

- Vollständige englische Fassung `pdca-en.html`: Oberfläche, Beispiele, geführter Modus, Glossar, FAQ, Quiz, Exporte (Markdown, JSON, Obsidian)
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

Alle Fixes im Code mit `// FIX (Toolkit): …` markiert. IDs, Datenformat (`D`: `meta`, `kpi`, `cycles[]`, `cur`), localStorage-Schlüssel (`pdcaW1T3.v1.*`), Exportstruktur und alle Credits (John Naska, mokka.solutions, Quellen) unverändert.

Hinweis zum Smoke-Test: `EXAMPLES` hat kein `loadExample()`. Beispiele werden über das Auswahlfeld `#exampleSel` → `loadKey('ex:<id>')` geladen; das funktioniert für alle 4 Beispiele.

#### Behobene Fehler

##### 1. Wiederhergestellter Entwurf galt als „gespeichert“ und ging beim nächsten Neuladen verloren
- **Fehler:** Nach einem Neuladen stellt `init()` den letzten Arbeitsstand aus dem Entwurf (`K_DRAFT`) wieder her, ruft danach aber `clearDirty()` auf. Das löscht den Entwurf und markiert den Stand als gespeichert (kein Punkt, kein „noch nicht gespeichert“). Beim nächsten Neuladen lädt `K_LAST` (Beispiel/Projekt) – die Eingaben sind weg.
- **Fix:** Merken, ob der Stand aus dem Entwurf kam. Weicht er inhaltlich (ohne den aktuell geöffneten Durchlauf `cur`) von der Basis (Projekt oder Vorlage) ab, `markDirty()` aufrufen – der Entwurf wird neu geschrieben, der Status zeigt „noch nicht gespeichert“. Ein reiner Navigations-Entwurf (Durchlauf gewechselt) gilt weiterhin als unverändert.
- **Geprüft:** Thema eingetippt → Entwurf → `init()` (Neuladen): vorher `dirty=false`, Entwurf gelöscht, nach 2. Neuladen Thema leer. Jetzt `dirty=true`, Status „noch nicht gespeichert“, Thema nach 2. Neuladen noch da. Nur Durchlauf gewechselt → nicht dirty.

##### 2. „Rückgängig“ nach Entfernen eines Durchlaufs fügte ihn in ein anderes Vorhaben ein
- **Fehler:** Der Rückgängig-Toast von `deleteCycle()` (8 s sichtbar) fügte den entfernten Durchlauf in das aktuelle `D` ein – auch wenn inzwischen zu einem anderen Beispiel/Projekt gewechselt wurde.
- **Fix:** Rückgängig greift nur, wenn `D` noch dasselbe Objekt ist (und `MAX_CYC` nicht überschritten wird).
- **Geprüft:** Durchlauf 2 in „Produktion“ entfernt → zu „Alltag“ gewechselt → Rückgängig: vorher hatte Alltag 2 Durchläufe, jetzt 1. Rückgängig im selben Vorhaben funktioniert weiter (wieder 2 Durchläufe).

#### Ohne Befund geprüft
Alle 4 Beispiele (Leer, Produktion, Konditorei, Alltag), alle Durchläufe durchgeklickt; Soll-Ist-Rechnung (`calc`, Status teil/erreicht, Prozentpunkte bei %, Richtungsprüfung senken/erhöhen); `buildMarkdown/buildJSON/buildObsidian` + Import-Rundlauf (MD, JSON, Obsidian, Standalone-HTML) je Beispiel identisch; Datei-Import über die Oberfläche (MD, HTML mit eingebetteten Projekten); neuer Durchlauf mit Übernahme (Entscheidung „standard“ → Ergebnis wird neuer Ausgangswert, Ziel leer, „Neuer Standard aus Durchlauf n“ im Ist); `MAX_CYC`=12 eingehalten; Karten als erledigt markieren, Entscheidung mit angepassten A1-Leitfragen, Durchlauf entfernen + Rückgängig; Speichern als Projekt → Neuladen aus localStorage; Geführter Modus über alle 6 Schritte und alle Karten bis „fertig“; Bericht inkl. Diagramm. Kein NaN/undefined, keine Konsolenfehler.

#### Aufgefallen, nicht geändert
- Projekt-IDs aus importierten/eingebetteten Dateien werden nicht mit `SAFE_ID` geprüft (anders als beim Laden aus localStorage). Im Test führte `__proto__` zu keinem sichtbaren Fehler (wird unter neuer ID abgelegt). Eine Prüfung wurde testweise ergänzt und wieder entfernt, da kein realer Fehler vorlag.
- `showStorageFullWarning()` setzt `storeOK=false` für die ganze Sitzung. Nach einmal vollem Speicher bleibt Speichern bis zum Neuladen gesperrt, auch wenn alte Projekte gelöscht werden.

## 1.0.0 – Original (John Naska)

Unveränderte Fassung aus dem Kurs, so wie sie John Naska (mokka.solutions) erstellt hat. Als HTML-Datei im Release [pdca-v1.0.0](https://github.com/milad-karami/lean-ci-kaizen-tools/releases/tag/pdca-v1.0.0) verfügbar.
