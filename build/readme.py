#!/usr/bin/env python3
"""Erzeugt README.md (Englisch + Deutsch) aus build/toolkit.json.

Usage:  python3 build/readme.py
Tool-Karten, Versionen und Links kommen aus der Konfiguration; Screenshots aus docs/screenshots/tools/<id>.png.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "build" / "toolkit.json").read_text(encoding="utf-8"))
LIVE = "https://milad-karami.github.io/lean-ci-kaizen-tools/"
REPO = "https://github.com/milad-karami/lean-ci-kaizen-tools"
LINKEDIN = "https://www.linkedin.com/in/milad-karami-63075b78/"
N = len(CFG["tools"])

# (Tool-ID, Bildunterschrift EN, DE) – nur Bilder, die es gibt, werden gezeigt
GALLERY = [
    ("ishikawa", "Ishikawa – causes by 6M, rated and prioritised", "Ishikawa – Ursachen nach 6M, bewertet und priorisiert"),
    ("oee-rechner", "OEE – time cascade and loss analysis", "OEE – Zeitkaskade und Verlustanalyse"),
    ("swot-analyse", "SWOT & TOWS – from factors to strategies", "SWOT & TOWS – von Faktoren zu Strategien"),
    ("heijunka", "Heijunka – levelling volume and mix", "Heijunka – Menge und Mix nivellieren"),
    ("smed-rechner", "SMED – the three stages of changeover reduction", "SMED – die drei Stufen der Rüstzeitreduzierung"),
    ("kanban-regelkreislauf", "Kanban – live factory simulation", "Kanban – Fabrik-Simulation live"),
]


def en_href(t):
    return LIVE + "tools/" + (t.get("en_file") or f'{t["id"]}.html')


def de_href(t):
    return LIVE + f'tools/{t["id"]}.html'


def cell(t, lang):
    if lang == "en":
        links = f'<a href="{en_href(t)}"><b>Open</b></a>'
        if t.get("en_file"):
            links += f' · <a href="{de_href(t)}">Deutsch</a>'
        name, summ, main = t["en"], t["sum_en"], en_href(t)
    else:
        links = f'<a href="{de_href(t)}"><b>Öffnen</b></a>'
        if t.get("en_file"):
            links += f' · <a href="{en_href(t)}">English</a>'
        name, summ, main = t["de"], t["sum_de"], de_href(t)
    links += f' · <a href="changelog/{t["id"]}.md">v{t["version"]}</a>'
    img = (f'<a href="{main}"><img src="assets/illustrations/{t["id"]}.webp" alt="{name}" width="100%"></a><br>'
           if (ROOT / "assets" / "illustrations" / f'{t["id"]}.webp').exists() else "")  # ohne Codex-Bild nur Text
    return (f'<td width="33%" valign="top">{img}<b>{name}</b><br><sub>{summ}</sub><br>{links}</td>')


def phases(lang):
    out = []
    for p in CFG["phases"]:
        tools = [t for t in CFG["tools"] if t["phase"] == p["id"]]
        rows = ["<tr>" + "".join(cell(t, lang) for t in tools[i:i + 3]) + "</tr>" for i in range(0, len(tools), 3)]
        out.append(f'### {p["n"]} · {p[lang]}\n*{p["q_" + lang]}*\n\n<table>\n' + "\n".join(rows) + "\n</table>\n")
    return "\n".join(out)


def table_de():
    rows = ["| Phase | Werkzeug | Wofür | Öffnen | Version |", "|---|---|---|---|---|"]
    for p in CFG["phases"]:
        for t in (t for t in CFG["tools"] if t["phase"] == p["id"]):
            links = f'[Öffnen]({de_href(t)})' + (f' · [English]({en_href(t)})' if t.get("en_file") else "")
            rows.append(f'| {p["n"]} · {p["short_de"]} | **{t["de"]}** | {t["sum_de"]} | {links} | [v{t["version"]}](changelog/{t["id"]}.md) |')
    return "\n".join(rows)


def gallery(lang):
    shots = [(i, en, de) for i, en, de in GALLERY if (ROOT / "docs" / "screenshots" / "tools" / f"{i}.png").exists()]
    rows = []
    for k in range(0, len(shots), 2):
        tds = "".join(f'<td width="50%" valign="top"><img src="docs/screenshots/tools/{i}.png" alt="{en}" width="100%">'
                      f'<br><sub>{en if lang == "en" else de}</sub></td>' for i, en, de in shots[k:k + 2])
        rows.append(f"<tr>{tds}</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>" if rows else ""


def path_line(lang):
    return " → ".join(f'**{p["n"]} {p["short_" + lang]}**' for p in CFG["phases"])


all_en = all(t.get("en_file") for t in CFG["tools"])
lang_en = "Every tool in **English and German**" if all_en else "Tools in German, Kanban also in English"
lang_de = "Jedes Tool auf **Englisch und Deutsch**" if all_en else "Tools auf Deutsch, Kanban auch auf Englisch"

README = f"""<div align="center">

<a href="{LIVE}"><img src="assets/logo-wordmark.svg" alt="Lean · CI · Kaizen Toolkit" width="300"></a>

### {N} free, interactive tools for Lean, continuous improvement, Six Sigma and Kaizen – organised along the improvement process.

[![Live demo](https://img.shields.io/badge/%E2%96%B6%20Live%20demo-open%20in%20browser-f2c94c?style=for-the-badge&labelColor=14213d)]({LIVE})
[![Tools](https://img.shields.io/badge/tools-{N}-3b6fd6?style=for-the-badge&labelColor=14213d)](#the-tools-along-the-improvement-process)
[![Releases](https://img.shields.io/badge/versions-releases-ef7fb3?style=for-the-badge&labelColor=14213d)]({REPO}/releases)

**🇬🇧 English** · 🇩🇪 [Deutsch](#deutsch)

<a href="{LIVE}"><img src="docs/screenshots/hub.png" alt="Lean · CI · Kaizen Toolkit – start page" width="100%"></a>

</div>

## Why this toolkit

Improvement projects fail less often because of missing knowledge than because of missing structure. This toolkit puts {N}
proven methods in the order you actually need them – from understanding the context to sustaining the result – and makes
each one hands-on: enter your own data, see the result immediately and hand over a clean PDF report.

- **Free and private** – runs completely in your browser, no account, no server, your data stays on your device
- **No installation** – every tool is a single HTML file that also works offline
- **Guided** – step-by-step mode, worked examples, glossary, FAQ and quiz in every tool
- **Report-ready** – 📄 PDF report with selectable sections; export as Markdown, JSON or Obsidian note
- **Bilingual** – {lang_en}

## The tools along the improvement process

The phases follow **DMAIC** – the Six Sigma improvement cycle – with a strategic context phase in front:
{path_line("en")}. Click a picture to open the tool.

{phases("en")}
### ★ My own tools
*Developed by Milad Karami, outside the improvement path.*

- **[Prozessnavigator](https://milad-karami.github.io/lean-ci-kaizen-tools/my-tools/prozessnavigator.html)** – process description (ISO 9001), RASIC matrix and flowcharts in one place; exports a complete Excel file with real flowchart shapes and collapsible groups (+ / −), optionally only for clean-room or grey-room customers. *(German)*

## Inside the tools

{gallery("en")}

## How to use

1. **Online:** open the [live demo]({LIVE}) and pick a phase – or jump straight to a tool above.
2. **Work:** start from a worked example or an empty template; your work is saved automatically in your browser.
3. **Report:** click **📄 Report (PDF)**, choose the sections and select **Save as PDF** in the print dialog (best in Chrome or Edge).
4. **Offline:** download the complete toolkit from the [latest release]({REPO}/releases/latest) (zip) or any single file from [`tools/`](tools/) and double-click it.

## Versions & changelog

Every tool has its own version and change log – what changed and which bugs were fixed compared to the original:
see the version links above or the [`changelog/`](changelog/) folder. All versions, including the **unchanged originals (v1.0.0)**,
are available as single HTML files under [**Releases**]({REPO}/releases) (tags `<tool>-v<version>`, e.g. `oee-rechner-v1.0.0`).
The complete website is released as `toolkit-v<version>`.

## Origin, authorship & permission

- **Original tools:** John Naska, [mokka.solutions](https://www.mokka.solutions/) – created for a Lean / CI training course.
  The structure, content and logic of the original tools are his work.
- **Further development:** [Milad Karami]({LINKEDIN}), October 2026 – toolkit structure along the improvement process,
  unified design, PDF report, English versions, versioning and bug fixes (documented per tool in [`changelog/`](changelog/)).
- Published **with the permission of John Naska**, crediting him by name and marking all changes.
- Subject-matter sources (videos, literature) are linked in each tool; all rights remain with their creators.

## License

This repository has **no open-source license**. All rights to the original tools remain with John Naska (mokka.solutions).
Using the tools for learning is explicitly welcome. If you pass them on or develop them further, please keep the chain of
origin visible: John Naska (mokka.solutions) → this version (Milad Karami), each with a short description of your own changes.

---

<a id="deutsch"></a>

## Deutsch

**{N} kostenlose, interaktive Werkzeuge für Lean, KVP, Six Sigma und Kaizen – geordnet entlang des Verbesserungsprozesses.**
[Live-Demo öffnen]({LIVE}) und oben rechts „🇩🇪 Deutsch“ wählen.

- **Kostenlos und privat** – läuft komplett im Browser, ohne Konto und Server; deine Daten bleiben auf deinem Gerät
- **Ohne Installation** – jedes Tool ist eine einzelne HTML-Datei und läuft auch offline
- **Geführt** – Schritt-für-Schritt-Modus, Beispiele, Glossar, FAQ und Quiz in jedem Tool
- **Berichtsfertig** – 📄 PDF-Bericht mit wählbaren Abschnitten; Export als Markdown, JSON oder Obsidian-Notiz
- **Zweisprachig** – {lang_de}

### Die Werkzeuge entlang des Verbesserungsprozesses

Die Phasen folgen **DMAIC** mit vorgeschalteter Kontext-Phase: {path_line("de")}.

{table_de()}

**★ Eigene Tools** (von Milad Karami, außerhalb des Verbesserungswegs): [Prozessnavigator](https://milad-karami.github.io/lean-ci-kaizen-tools/my-tools/prozessnavigator.html) – Prozessbeschreibung, RASIC und Flowcharts, Export als Excel mit aufklappbarer Gliederung.

### Einblick in die Tools

{gallery("de")}

### Nutzung

1. **Online:** [Live-Demo]({LIVE}) öffnen und eine Phase wählen – oder oben direkt ein Tool öffnen.
2. **Arbeiten:** mit einem Beispiel oder einer leeren Vorlage starten; der Stand wird automatisch im Browser gespeichert.
3. **Bericht:** „📄 Bericht (PDF)“ → Abschnitte wählen → im Druckdialog „Als PDF sichern“ (am besten in Chrome oder Edge).
4. **Offline:** das komplette Toolkit aus dem [neuesten Release]({REPO}/releases/latest) (zip) oder eine einzelne Datei aus [`tools/`](tools/) herunterladen und per Doppelklick öffnen.

### Versionen & Änderungsprotokoll

Jedes Tool hat eine eigene Version und ein eigenes Änderungsprotokoll – was sich gegenüber dem Original geändert hat und welche
Fehler behoben wurden: siehe die Versions-Links oben oder den Ordner [`changelog/`](changelog/). Alle Versionen, auch die
**unveränderten Originale (v1.0.0)**, gibt es als einzelne HTML-Datei unter [**Releases**]({REPO}/releases).

### Herkunft, Urheberschaft & Genehmigung

- **Original-Tools:** John Naska, [mokka.solutions](https://www.mokka.solutions/) – erstellt für einen Lean-/KVP-Kurs.
- **Weiterentwicklung:** [Milad Karami]({LINKEDIN}), Oktober 2026 – Toolkit-Struktur, einheitliches Design, PDF-Bericht,
  englische Fassungen, Versionierung und Fehlerkorrekturen.
- Veröffentlicht **mit Genehmigung von John Naska**, unter Nennung seines Namens und mit Kennzeichnung aller Änderungen.

### Lizenz

Keine Open-Source-Lizenz. Die Rechte an den Original-Tools liegen bei John Naska (mokka.solutions). Die Nutzung zum Lernen ist
ausdrücklich erwünscht. Bei Weitergabe bitte die Herkunftskette nennen: John Naska (mokka.solutions) → diese Fassung (Milad Karami).
"""

if __name__ == "__main__":
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    print(f"README.md written: {len(README) // 1024} KB")
