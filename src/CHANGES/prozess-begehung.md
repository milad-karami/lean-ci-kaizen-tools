# prozess-begehung.html – Änderungen (Toolkit)

Der Fix ist im CSS mit `/* FIX (Toolkit): … */` markiert. IDs, Datenformat (`meta`, `st`, `m`, `done`, dazu `st.ito`, `st.sz`, `st.frag_hilfe` als JSON-Text), localStorage-Schlüssel (`begehungW1T1.v2.*`), Exportstruktur, die eingebetteten Bibliotheken (draw.io-Viewer, bpmn-js, diagram-js, Schriften), die CSP und alle Credits (John Naska, mokka.solutions, Quellen) bleiben unverändert.

## Hinweis aus dem Smoke-Test: `EXAMPLES` ohne `loadExample()`

Das ist kein Fehler. Die Beispiele werden über die Auswahl „Vorlagen (Basis)“ (`#exampleSel` → `loadKey('ex:<id>')`) geladen. Im Browser geprüft: „Eigene Begehung (leer)“, „Produktionsbetrieb“ und „Dienstleister / Backoffice“ laden jeweils vollständig (Stammdaten, 19 Textfelder, ITO-Diagramm, Fragilität, Erledigt-Status).

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Auf schmalen Bildschirmen (375 px) waren die Bedienhinweise über dem Input-Transformation-Output-Diagramm (Werkzeug 1 · Karte 4) rechts abgeschnitten, z. B. „…auf die Fläche zi“. | `.it-tipp span{white-space:nowrap}` – die Hinweise sind länger als die Karte (≈ 280 px), und `.gcard` schneidet mit `overflow:hidden` ab. | Unter 640 px dürfen die Hinweise umbrechen (`@media (max-width:640px){.it-tipp span{white-space:normal}}`). Am Desktop ändert sich nichts. | Auf `main` per Screenshot reproduziert. Nach dem Fix vollständig lesbar. Die automatische Prüfung auf abgeschnittene Elemente ist bei 375 px und 1920 px in allen Tabs leer. |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler oder -warnungen, auch keine CSP-Verletzungen. Das ITO-Diagramm (bpmn-js) wird gezeichnet.
- Alle 3 Vorlagen über die Auswahl geladen. Jeden sichtbaren Bedienknopf angeklickt:
  - Erledigt-Status aller 13 Karten
  - Fragilität Fragil/Robust/Resilient/Antifragil
  - „+ Input / + Wertstrom / + Output“
  - Diagramm-Zoom und Vollbild
  - „Schnittstelle anlegen“
  - Fragilitäts-Hilfe (Dialog)
  - Sprünge aus dem Bericht
- Geführter Modus bis „fertig“, Tabs FAQ, Quiz und Netz.
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jede Vorlage. Der Re-Import aller drei Formate ergibt jeweils exakt den Stand, einschließlich ITO, Schnittstellen und Erledigt-Status. Der Import einer Markdown-Datei über den echten `#importFile`-Handler funktioniert.
- Eingabe (auto-angelegte Begehung) → Autosave → Neuladen → Öffnen ergibt einen identischen Stand.
- Quiz: eine komplette Runde mit 20 Fragen bis zur Auswertung, ohne Fehler.
- Layout bei 375 px und 1920 px in allen Tabs: kein horizontaler Seiten-Scroll, nach dem Fix keine abgeschnittenen Elemente.
