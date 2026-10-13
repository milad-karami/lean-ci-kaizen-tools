#!/usr/bin/env python3
"""Baut die Toolkit-Fassung aller Tools: src/tools/*.html + gemeinsame Ebene -> tools/*.html.

Usage:  python3 build/build.py
Die gemeinsame Ebene (Top-Leiste, Hero im Toolkit-Look, Illustration, PDF-Bericht, Footer-Hinweis) wird
eingefügt, ohne den Code der Tools zu verändern. Änderungen an den Tools selbst gehören nach src/tools/.
"""
import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B = ROOT / "build"
CFG = json.loads((B / "toolkit.json").read_text(encoding="utf-8"))
CSS = (B / "layer.css").read_text(encoding="utf-8")
JS = (B / "layer.js").read_text(encoding="utf-8")

PLACEHOLDER_LOGO = ('<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
                    '<circle cx="32" cy="32" r="24" fill="none" stroke="#f2c94c" stroke-width="6" stroke-dasharray="34 4"/>'
                    '<rect x="25" y="22" width="14" height="20" rx="3" fill="#ef7fb3"/></svg>')


def read_svg(path, fallback=""):
    if not path.exists():
        return fallback
    s = path.read_text(encoding="utf-8")
    s = re.sub(r"<\?xml[^>]*\?>", "", s)
    s = re.sub(r"<!DOCTYPE[^>]*>", "", s)
    return s.strip()


LOGO = read_svg(ROOT / "assets" / "logo.svg", PLACEHOLDER_LOGO)
PHASES = {p["id"]: p for p in CFG["phases"]}
TOOLS = CFG["tools"]

T = {
    "de": {"all": "Alle Tools", "prev": "Vorheriges Tool", "next": "Nächstes Tool", "phase": "Phase",
           "toolkit": "Toolkit", "nav": "Toolkit-Navigation",
           "dl_t": "Dieses Tool als HTML-Datei herunterladen – läuft offline, ohne Installation"},
    "en": {"all": "All tools", "prev": "Previous tool", "next": "Next tool", "phase": "Phase",
           "toolkit": "Toolkit", "nav": "Toolkit navigation",
           "dl_t": "Download this tool as an HTML file – works offline, no installation"},
}


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def js_json(obj):
    # sicher in <script> einbetten
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def brand_bar(tool, lang):
    t = T[lang]
    idx = TOOLS.index(tool)
    prev_t = TOOLS[idx - 1] if idx > 0 else None
    next_t = TOOLS[idx + 1] if idx < len(TOOLS) - 1 else None
    cur_n = PHASES[tool["phase"]]["n"]
    own = tool["en_file"] if lang == "en" and tool.get("en_file") else f'{tool["id"]}.html'
    steps = []
    for p in CFG["phases"]:
        cls = "cur" if p["n"] == cur_n else ("done" if p["n"] < cur_n else "")
        label = p["short_" + lang]
        cur_attr = ' aria-current="step"' if cls == "cur" else ""
        steps.append(f'<li class="{cls}"><a href="../index.html#phase-{p["id"]}" title="{esc(p[lang])}"'
                     f'{cur_attr}><i>{p["n"]}</i><span>{esc(label)}</span></a></li>')

    def nav_link(t2, cls, arrow, title):
        if not t2:
            return f'<a class="{cls}" aria-disabled="true">{arrow}</a>'
        name = t2[lang]
        href = t2["en_file"] if lang == "en" and t2.get("en_file") else f'{t2["id"]}.html'
        return (f'<a class="{cls}" href="{href}" title="{esc(title)}: {esc(name)}">'
                + (f'{arrow} <span class="tk-lbl">{esc(name)}</span>' if cls == "tk-prev" else f'<span class="tk-lbl">{esc(name)}</span> {arrow}')
                + '</a>')

    return (f'<nav class="tk-bar" aria-label="{t["nav"]}"><div class="tk-bar-in">'
            f'<a class="tk-brand" href="../index.html" title="Lean · CI · Kaizen Toolkit">{LOGO}'
            f'<span><b>Lean · CI · Kaizen</b><small>{t["toolkit"].upper()}</small></span></a>'
            f'<ol class="tk-steps">{"".join(steps)}</ol>'
            f'<div class="tk-nav"><a class="tk-dl" href="{own}" download="{own}" title="{esc(t["dl_t"])}">⬇ HTML</a>'
            f'{nav_link(prev_t, "tk-prev", "‹", t["prev"])}'
            f'<a class="tk-all" href="../index.html#tools">{t["all"]}</a>'
            f'{nav_link(next_t, "tk-next", "›", t["next"])}</div></div></nav>')


def footer_block(lang, tool):
    ver = changelog_link(tool, f'Version {tool["version"]}')
    if lang == "en":
        return ('<div class="fblock tk-credit"><h4>This toolkit version</h4>Further developed by '
                '<a href="https://www.linkedin.com/in/milad-karami-63075b78/" target="_blank" rel="noopener">Milad Karami</a> '
                '(October 2026): unified design, process navigation, PDF report and bug fixes. '
                f'{ver} ({esc(tool["version_name"])}) – {changelog_link(tool, "change log on GitHub")}. '
                'Original tool: John Naska (mokka.solutions), published with his permission.</div>')
    return ('<div class="fblock tk-credit"><h4>Diese Toolkit-Fassung</h4>Weiterentwickelt von '
            '<a href="https://www.linkedin.com/in/milad-karami-63075b78/" target="_blank" rel="noopener">Milad Karami</a> '
            '(Oktober 2026): einheitliches Design, Prozess-Navigation, PDF-Bericht und Fehlerkorrekturen. '
            f'{ver} ({esc(tool["version_name"])}) – {changelog_link(tool, "Änderungsprotokoll auf GitHub")}. '
            'Original-Tool: John Naska (mokka.solutions), veröffentlicht mit seiner Genehmigung.</div>')


def changelog_link(tool, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<a{c} href="https://github.com/milad-karami/lean-ci-kaizen-tools/blob/main/changelog/{tool["id"]}.md" '
            f'target="_blank" rel="noopener" title="Changelog">{esc(text)}</a>')


LI_SVG = ('<svg class="li" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 '
          '2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.2c0-1.24'
          '-.02-2.84-1.73-2.84-1.73 0-2 1.35-2 2.75V21h-4z"/></svg>')


def credit_row(tool, lang):
    """Kopfzeile wie im Kanban-Tool: LinkedIn, Sprachwechsel, Original-Tool."""
    if lang == "en":
        dev, li_t, other = "Development", "Milad Karami on LinkedIn", f'<a class="tm" href="{tool["id"]}.html" hreflang="de" title="Deutsche Version">🇩🇪 Deutsch</a>'
        orig, month = "Original tool", "October 2026"
    else:
        dev, li_t, orig, month = "Entwicklung", "Milad Karami auf LinkedIn", "Original-Tool", "Oktober 2026"
        other = f'<a class="tm" href="{tool["en_file"]}" hreflang="en" title="English version">🇬🇧 English</a>' if tool.get("en_file") else ""
    return (f'<div class="credit tk-cred"><span class="cl">{dev}</span><a class="tm dev" href="https://www.linkedin.com/in/milad-karami-63075b78/" '
            f'target="_blank" rel="noopener" title="{li_t}">{LI_SVG}Milad Karami</a>{other}'
            f'<span class="cl orig">{orig}: <b>John Naska</b> (<a href="https://www.mokka.solutions/" target="_blank" rel="noopener">mokka.solutions</a>) · {month}</span></div>')


def once(s, pattern, repl, what, flags=0):
    new, n = re.subn(pattern, repl, s, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"Einfügepunkt nicht gefunden: {what}")
    return new


def build_tool(tool, src_name, out_name, lang="de"):
    s = (ROOT / "src" / "tools" / src_name).read_text(encoding="utf-8")
    phase = PHASES[tool["phase"]]
    art_file = B / "art" / f'{tool["id"]}.webp'  # kleine Codex-Illustration, eingebettet (Tool bleibt eine Datei)
    art = (f'<img alt="" src="data:image/webp;base64,{base64.b64encode(art_file.read_bytes()).decode()}">'
           if art_file.exists() else "")
    special = tool.get("special") == "kanban"
    cfg = {"id": tool["id"], "title": tool[lang], "phaseN": phase["n"], "phaseName": phase[lang],
           "logo": LOGO, "art": art, "version": tool["version"], "lang": lang, "noReport": special}
    head = (f'<style id="tk-style">{CSS}</style>\n'
            f'<script id="tk-cfg">window.TK_CFG={js_json(cfg)};</script>\n'
            f'<script id="tk-layer">{JS}</script>\n')
    s = once(s, r"<body[^>]*>", lambda m: m.group(0) + "\n" + brand_bar(tool, lang), "<body>")
    chip = (f'<div class="tk-hero-art" aria-hidden="true">{art}</div>' if art else "") + \
           f'<div class="tk-phase"><i>{phase["n"]}</i>{T[lang]["phase"]} {phase["n"]} · {esc(phase[lang])}' \
           f'{changelog_link(tool, "v" + tool["version"], "tk-ver")}</div>'
    s = once(s, r'<header class="hero"[^>]*>', lambda m: m.group(0) + chip, "header.hero")
    if not special:
        s = once(s, r'(<header class="hero".*?<div class="kicker">.*?</div>)', lambda m: m.group(1) + credit_row(tool, lang),
                 "kicker", flags=re.S)
        s = once(s, r'<footer class="foot">', lambda m: m.group(0) + footer_block(lang, tool), "footer.foot")
    s = once(s, r"<title>([^<]*)</title>",
             lambda m: f"<title>{m.group(1)} · Lean · CI · Kaizen Toolkit</title>", "<title>")
    # Kopf-Einschub zuletzt: das Layer-Skript enthält selbst Tags wie <body> als Text
    s = once(s, r"</head>", lambda m: head + "</head>", "</head>")
    out = ROOT / "tools" / out_name
    out.write_text(s, encoding="utf-8")
    return out


def main():
    (ROOT / "tools").mkdir(exist_ok=True)
    built = []
    for tool in TOOLS:
        built.append(build_tool(tool, tool["src"], f'{tool["id"]}.html', "de"))
        if tool.get("en_file"):
            built.append(build_tool(tool, tool["en_file"], tool["en_file"], "en"))
    for p in built:
        print(f"built {p.relative_to(ROOT)}  ({p.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
