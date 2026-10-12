# Lean · CI · Kaizen Toolkit

**15 free, interactive tools for Lean, continuous improvement (CI / KVP), Six Sigma and Kaizen – organised along the improvement process, each with a PDF report. No installation, no account, works offline.**

[![Live demo](https://img.shields.io/badge/%E2%96%B6%20Live%20demo-open%20in%20browser-f2c94c?style=for-the-badge&labelColor=14213d)](https://milad-karami.github.io/lean-ci-kaizen-tools/)
[![Tools](https://img.shields.io/badge/tools-15-3b6fd6?style=for-the-badge&labelColor=14213d)](#tools)
[![PDF report](https://img.shields.io/badge/PDF%20report-in%20every%20tool-ef7fb3?style=for-the-badge&labelColor=14213d)](#how-to-use)

**🇬🇧 English** · 🇩🇪 [Deutsch](#deutsch)

<a href="https://milad-karami.github.io/lean-ci-kaizen-tools/"><img src="docs/screenshots/hub.png" alt="Lean · CI · Kaizen Toolkit – start page with the improvement process" width="100%"></a>

## Tools

The tools follow **DMAIC** – the Six Sigma improvement cycle – with a strategic context phase in front:
**Context → Define → Measure → Analyze → Improve → Control.** Every tool has the same toolkit header (process navigation,
previous / next tool), a **📄 PDF report** with selectable sections, saving of your work in the browser and Markdown /
JSON / Obsidian export. The tools are in German; the Kanban simulation is also available in English.

| Phase | Tool | What it does | Open | Version |
|---|---|---|---|---|
| 0 · Context & strategy | **STEP / PEST analysis** | Scan the macro environment: social, technological, economic and political factors. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/step-analyse.html) | [v2.0.0](changelog/step-analyse.md) |
| 0 · Context & strategy | **Five Forces** | Porter's industry structure: rivalry, suppliers, buyers, new entrants, substitutes. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/five-forces.html) | [v2.0.0](changelog/five-forces.md) |
| 0 · Context & strategy | **SWOT analysis (incl. TOWS)** | Strengths, weaknesses, opportunities, threats – turned into strategic options. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/swot-analyse.html) | [v2.0.0](changelog/swot-analyse.md) |
| 1 · Define | **SIPOC** | Scope the process: suppliers, inputs, process steps, outputs, customers. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/sipoc.html) | [v2.0.0](changelog/sipoc.md) |
| 1 · Define | **Kano model** | Classify customer requirements: basic, performance and delighter features. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kano-modell.html) | [v2.0.0](changelog/kano-modell.md) |
| 1 · Define | **CTQ analysis** | Translate the voice of the customer into measurable critical-to-quality specs. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ctq-analyse.html) | [v2.0.0](changelog/ctq-analyse.md) |
| 2 · Measure | **Process walk-through (Gemba)** | Capture the process on site: think in systems, observe, document. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-begehung.html) | [v2.0.0](changelog/prozess-begehung.md) |
| 2 · Measure | **OEE calculator** | Overall equipment effectiveness = availability × performance × quality – with loss analysis. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/oee-rechner.html) | [v2.0.0](changelog/oee-rechner.md) |
| 3 · Analyze | **Value stream mapping (current & future)** | Make material and information flow visible, find lead time and waste. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/wertstromanalyse.html) | [v2.0.0](changelog/wertstromanalyse.md) |
| 3 · Analyze | **Ishikawa diagram** | Collect and rate causes systematically (6M) – instead of treating symptoms. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ishikawa.html) | [v2.0.0](changelog/ishikawa.md) |
| 4 · Improve | **SMED calculator** | Cut changeover time: move internal to external steps, parallelise, standardise. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/smed-rechner.html) | [v2.0.0](changelog/smed-rechner.md) |
| 4 · Improve | **EPEI calculator** | Every part every interval: derive lot size and supermarket from changeover and capacity. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/epei-rechner.html) | [v2.0.0](changelog/epei-rechner.md) |
| 4 · Improve | **Heijunka** | Level production by volume and mix – a steady flow instead of waves. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/heijunka.html) | [v2.0.0](changelog/heijunka.md) |
| 4 · Improve | **Kanban control loops** | Pull simulation with an animated factory, optimisation to zero shortages and changeover time. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-regelkreislauf.html) · [English](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-control-loops.html) | [v2.2.0](changelog/kanban-regelkreislauf.md) |
| 5 · Control | **PDCA cycle** | Plan – Do – Check – Act: secure improvements, standardise and keep turning. | [Open (DE)](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/pdca.html) | [v2.0.0](changelog/pdca.md) |


---

## Versions & changelog

Every tool has its own version number and change log – what changed and which bugs were fixed compared to John Naska's original:
see the **Version** column above or the [`changelog/`](changelog/) folder. All versions, including the **unchanged originals (v1.0.0)**,
can be downloaded as single HTML files from [**Releases**](https://github.com/milad-karami/lean-ci-kaizen-tools/releases) (tags `<tool>-v<version>`, e.g. `oee-rechner-v1.0.0`).
The complete website is released as `toolkit-v<version>`.

## Kanban control loops – a guided tour

The tool simulates a **leveling withdrawal kanban**, step by step:
customer withdrawal → lot size formation post → sequenced kanban chute → 4 stations (one-piece flow) → loading cart → product store → shipping.
You set demand, product store size (number of kanban cards) and lot size, press **▶ Play** and watch the loop work. Or watch it break.

### 🏭 Live factory: see what the numbers mean

An animated factory scene runs in sync with the simulation. Workers move when their station is busy, the “Changeover!” bubble appears when a new variant arrives, the loading cart brings finished lots back, boxes fly to shipping, the truck leaves when a pallet is full, and an alarm goes off on a shortage.

![Animated factory scene with four workers, product store, lot post, shipping area and truck](docs/screenshots/factory.png)

### 🧭 Step-by-step flow with live explanation

A 7-step flow bar highlights what is happening right now, and a plain-language narration explains every takt.

![Seven-step flow bar and live narration](docs/screenshots/flow.png)

### 📋 The full board: schedule, product store, chute, lot post, line

Everything from the original training board in one place. Shortages are marked in red in the withdrawing schedule. Every section can be rearranged by **drag & drop**.

<details>
<summary>Show the full board</summary>

![Withdrawing schedule, product store, live factory, chute, lot size formation post and production line](docs/screenshots/board.png)

</details>

### ✨ Optimize: zero shortages with the fewest cards

One click searches for the smallest number of kanban cards that still serves every customer request. It can optionally optimize the lot size too, explains the rule behind the result, and has *Undo* and *Play results* buttons.

![Optimization result: 13 shortages reduced to 0](docs/screenshots/optimize.png)

### 📄 PDF report for managers and customers

Choose what goes into the report: cover page, management summary with traffic light, KPIs explained in plain language, configuration, process diagram, inventory chart, problems, recommendation, factory view, glossary and sources. Then save it as a PDF.

<p>
  <img src="docs/screenshots/report-dialog.png" alt="Report dialog with selectable sections" width="32%">
  &nbsp;
  <img src="docs/screenshots/report-pages.png" alt="Pages of the PDF report" width="64%">
</p>

### More features

- **Changeover time:** set how many takts the line stops at every variant change. With 0 the changeover runs without a stop (as in the video). Higher values show why larger lots or bigger stores pay off, and ✨ Optimize takes it into account
- Pallet size freely selectable or coupled to the lot size
- Four ready-made scenarios (video scenario, balanced case, bottleneck case, your own scenario)
- Floating mini player; the page stays scrollable while the simulation runs
- Glossary (“terms explained simply”), FAQ and a quiz
- Save and load simulations; export as Markdown, JSON or Obsidian note
- English and German version, linked to each other

## How to use

- **Online:** open the [live demo](https://milad-karami.github.io/lean-ci-kaizen-tools/).
- **Offline:** download any file from the [`tools/`](tools/) folder and double-click it. It works in Chrome, Edge, Firefox and Safari.
- **PDF report:** click **📄 Report (PDF)**, select sections, then choose **Save as PDF** in the print dialog. Chrome and Edge give the best result.

## Origin, authorship & permission

- **Original tool:** John Naska, [mokka.solutions](https://www.mokka.solutions/). The structure, simulation logic and interface of the original tool are his work.
- **Subject-matter basis:** explainer video [“Leveling withdraw Kanban”](https://www.youtube.com/watch?v=buD22g8wNWw). The video is only linked, not embedded or copied. All rights remain with its creators.
- **Further development:** [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/), October 2026.
- Published **with the permission of John Naska**, crediting him by name and marking all changes.

<details>
<summary><b>Changes compared to the original</b></summary>

**2026-10-09**
- Logic bugs fixed:
  - pallet size selectable instead of a fixed 4
  - the line keeps flowing when there are gaps
  - deadlock detection when the number of kanban cards is smaller than the lot size
  - the shortage verdict is only “green” at zero shortages
  - the safety limit scales with demand
- New “✨ Optimize” function (zero shortages with the minimum number of kanban cards)
- Animated factory scene with cartoon illustrations, live narration, 7-step flow bar
- PDF report with selectable sections
- Drag & drop of sections, mini player; the page stays scrollable while playing

**2026-10-10**
- English version of the tool; English is now the default, German stays available
- New parameter **changeover time** (takts of line stop per variant change), included in KPIs, narration, exports and the PDF report

</details>

## License

This repository has **no open-source license**. All rights to the original tool remain with John Naska (mokka.solutions).
Using the tools for learning is explicitly welcome. If you develop the tool further or pass it on, please keep the chain of origin visible: video → John Naska (mokka.solutions) → this version (Milad Karami), each with the date and a short description of your own changes.

---

## Deutsch

**15 kostenlose, interaktive Werkzeuge zu Lean, KVP, Six Sigma und Kaizen – entlang des Verbesserungsprozesses (Kontext → Define → Measure → Analyze → Improve → Control), jedes mit PDF-Bericht. Ohne Installation, ohne Konto, auch offline.**

| Phase | Werkzeug | Wofür | Öffnen | Version |
|---|---|---|---|---|
| 0 · Kontext & Strategie | **STEP- / PEST-Analyse** | Makro-Umfeld systematisch scannen: soziale, technologische, ökonomische und politische Einflüsse. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/step-analyse.html) | [v2.0.0](changelog/step-analyse.md) |
| 0 · Kontext & Strategie | **Five Forces** | Branchenstruktur nach Porter: Rivalität, Lieferanten, Kunden, neue Anbieter, Substitute. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/five-forces.html) | [v2.0.0](changelog/five-forces.md) |
| 0 · Kontext & Strategie | **SWOT-Analyse (inkl. TOWS)** | Stärken, Schwächen, Chancen, Risiken – und daraus strategische Optionen ableiten. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/swot-analyse.html) | [v2.0.0](changelog/swot-analyse.md) |
| 1 · Define · Definieren | **SIPOC** | Den Prozess abgrenzen: Lieferanten, Inputs, Prozessschritte, Outputs, Kunden. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/sipoc.html) | [v2.0.0](changelog/sipoc.md) |
| 1 · Define · Definieren | **Kano-Modell** | Kundenanforderungen einordnen: Basis-, Leistungs- und Begeisterungsmerkmale. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kano-modell.html) | [v2.0.0](changelog/kano-modell.md) |
| 1 · Define · Definieren | **CTQ-Analyse** | Die Stimme des Kunden in messbare, qualitätskritische Merkmale übersetzen. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ctq-analyse.html) | [v2.0.0](changelog/ctq-analyse.md) |
| 2 · Measure · Messen | **Prozess-Begehung (Gemba)** | Den Prozess vor Ort erfassen: systemisch denken, beobachten, dokumentieren. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/prozess-begehung.html) | [v2.0.0](changelog/prozess-begehung.md) |
| 2 · Measure · Messen | **OEE-Rechner** | Gesamtanlageneffektivität = Verfügbarkeit × Leistung × Qualität – mit Verlustanalyse. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/oee-rechner.html) | [v2.0.0](changelog/oee-rechner.md) |
| 3 · Analyze · Analysieren | **Wertstromanalyse (IST & SOLL)** | Material- und Informationsfluss sichtbar machen, Durchlaufzeit und Verschwendung finden. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/wertstromanalyse.html) | [v2.0.0](changelog/wertstromanalyse.md) |
| 3 · Analyze · Analysieren | **Ishikawa-Diagramm** | Ursachen strukturiert sammeln und bewerten (6M) – statt nur Symptome zu behandeln. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/ishikawa.html) | [v2.0.0](changelog/ishikawa.md) |
| 4 · Improve · Verbessern | **SMED-Rechner** | Rüstzeit verkürzen: interne in externe Schritte verlagern, parallelisieren, standardisieren. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/smed-rechner.html) | [v2.0.0](changelog/smed-rechner.md) |
| 4 · Improve · Verbessern | **EPEI-Rechner** | Every Part Every Interval: Losgröße und Supermarkt aus Rüstzeit und Kapazität ableiten. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/epei-rechner.html) | [v2.0.0](changelog/epei-rechner.md) |
| 4 · Improve · Verbessern | **Heijunka** | Produktion nach Menge und Variantenmix nivellieren – gleichmäßiger Fluss statt Wellen. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/heijunka.html) | [v2.0.0](changelog/heijunka.md) |
| 4 · Improve · Verbessern | **Kanban-Regelkreisläufe** | Pull-Simulation mit animierter Fabrik, Optimierung auf 0 Fehlmengen und Rüstzeit. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-regelkreislauf.html) · [Englisch](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/kanban-control-loops.html) | [v2.2.0](changelog/kanban-regelkreislauf.md) |
| 5 · Control · Sichern | **PDCA-Zyklus** | Plan – Do – Check – Act: Verbesserungen absichern, standardisieren und weiterdrehen. | [Öffnen](https://milad-karami.github.io/lean-ci-kaizen-tools/tools/pdca.html) | [v2.0.0](changelog/pdca.md) |

### Versionen & Änderungsprotokoll

Jedes Tool hat eine eigene Versionsnummer und ein eigenes Änderungsprotokoll – was sich gegenüber dem Original von John Naska geändert hat
und welche Fehler behoben wurden: siehe Spalte **Version** oben oder den Ordner [`changelog/`](changelog/). Alle Versionen, auch die
**unveränderten Originale (v1.0.0)**, gibt es als einzelne HTML-Datei unter [**Releases**](https://github.com/milad-karami/lean-ci-kaizen-tools/releases) (Tags `<tool>-v<version>`,
z. B. `oee-rechner-v1.0.0`). Die gesamte Website erscheint als `toolkit-v<version>`.

### Funktionen

- Pull-Simulation eines Leveling-Withdraw-Kanban (Heijunka): Entnahme → Lot-Post → Chute → 4 Stationen (One-Piece-Flow) → Loading cart → Versand
- Animierte Szene „Fabrik live“: Werker, Rüstwechsel, Loading cart, LKW, Fehlmengen-Alarm
- Schritt-für-Schritt-Ablauf mit Live-Erklärung
- **✨ Optimieren:** kleinste Kanban-Anzahl mit 0 Fehlmengen (optional auch die Losgröße)
- **Rüstzeit:** wie viele Takte die Linie bei jedem Variantenwechsel stillsteht. Bei 0 läuft das Rüsten ohne Stopp (wie im Video). Fließt in Kennzahlen, Optimierung, Export und PDF-Bericht ein
- **📄 PDF-Bericht** für Führungskräfte und Kunden mit wählbaren Inhalten
- Bereiche per Drag & Drop, Mini-Player, Glossar, FAQ, Quiz, Speichern und Export

Die Screenshots oben zeigen die englische Fassung. Die deutsche Fassung ist inhaltlich identisch.

### Nutzung

- **Online:** [Live-Demo](https://milad-karami.github.io/lean-ci-kaizen-tools/) öffnen und oben rechts „🇩🇪 Deutsch“ wählen.
- **Offline:** [`kanban-regelkreislauf.html`](kanban-regelkreislauf.html) herunterladen und per Doppelklick öffnen.
- **PDF-Bericht:** „📄 Bericht (PDF)“ → Inhalte wählen → im Druckdialog „Als PDF sichern“.

### Herkunft, Urheberschaft & Genehmigung

- **Original-Tool:** John Naska, [mokka.solutions](https://www.mokka.solutions/)
- **Fachliche Grundlage:** Erklärvideo [„Leveling withdraw Kanban“](https://www.youtube.com/watch?v=buD22g8wNWw). Das Video ist nur verlinkt. Die Rechte daran liegen bei den jeweiligen Urheberinnen und Urhebern.
- **Weiterentwicklung:** [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/), Oktober 2026
- Veröffentlicht **mit Genehmigung von John Naska**, unter Nennung seines Namens und mit Kennzeichnung der Änderungen (siehe „Changes compared to the original“ oben).

### Lizenz

Keine Open-Source-Lizenz. Die Rechte am Original-Tool liegen bei John Naska (mokka.solutions). Die Nutzung zum Lernen ist ausdrücklich erwünscht. Bei Weitergabe bitte die Herkunftskette nennen: Video → John Naska (mokka.solutions) → diese Fassung (Milad Karami).
