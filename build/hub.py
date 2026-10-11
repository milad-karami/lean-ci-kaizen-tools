#!/usr/bin/env python3
"""Erzeugt die Startseite index.html (Hub) aus build/toolkit.json. Usage: python3 build/hub.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "build" / "toolkit.json").read_text(encoding="utf-8"))
BASE = "https://milad-karami.github.io/lean-ci-kaizen-tools/"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def bi(en, de, tag="span"):
    return f'<{tag} class="en">{esc(en)}</{tag}><{tag} class="de">{esc(de)}</{tag}>'


def card(t):
    href = f'tools/{t["id"]}.html'
    langs = '<span class="pill">DE</span>' + ('<span class="pill">EN</span>' if t.get("en_file") else "")
    en_link = (f'<a class="alt en" href="tools/{t["en_file"]}">English version →</a>'
               f'<a class="alt de" href="tools/{t["en_file"]}">Englische Version →</a>') if t.get("en_file") else ""
    return (f'<article class="card"><a class="hit" href="{href}" aria-label="{esc(t["en"])}"></a>'
            f'<div class="art"><img src="assets/illustrations/{t["id"]}.svg" alt="" loading="lazy" width="480" height="300"></div>'
            f'<div class="cb"><h3>{bi(t["en"], t["de"])}</h3><p>{bi(t["sum_en"], t["sum_de"])}</p>'
            f'<div class="meta">{langs}<span class="pill gold">PDF</span>'
            f'<span class="go">{bi("Open →", "Öffnen →")}</span></div>{en_link}</div></article>')


def phase_section(p):
    tools = [t for t in CFG["tools"] if t["phase"] == p["id"]]
    return (f'<section class="phase" id="phase-{p["id"]}"><div class="ph-head"><span class="ph-n">{p["n"]}</span>'
            f'<div><h2>{bi(p["en"], p["de"])}</h2><p class="q">{bi(p["q_en"], p["q_de"])}</p></div>'
            f'<span class="ph-count">{len(tools)} {bi("tools" if len(tools) != 1 else "tool", "Tools" if len(tools) != 1 else "Tool")}</span></div>'
            f'<div class="grid">{"".join(card(t) for t in tools)}</div></section>')


def stepper():
    items = []
    for p in CFG["phases"]:
        n = sum(1 for t in CFG["tools"] if t["phase"] == p["id"])
        items.append(f'<li><a href="#phase-{p["id"]}"><i>{p["n"]}</i><b>{bi(p["short_en"], p["short_de"])}</b>'
                     f'<small>{n} {bi("tools" if n != 1 else "tool", "Tools" if n != 1 else "Tool")}</small></a></li>')
    return f'<ol class="steps">{"".join(items)}</ol>'


N_TOOLS = len(CFG["tools"])
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lean · CI · Kaizen Toolkit – {N_TOOLS} interactive tools along the improvement process</title>
<meta name="description" content="{N_TOOLS} free interactive Lean, continuous improvement (CI/KVP), Six Sigma and Kaizen tools, organised along the improvement process (DMAIC) – each with a PDF report. Runs in your browser.">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}">
<meta property="og:title" content="Lean · CI · Kaizen Toolkit – {N_TOOLS} free interactive tools">
<meta property="og:description" content="From context to control: STEP, SWOT, SIPOC, Kano, CTQ, Gemba, OEE, value stream, Ishikawa, SMED, EPEI, Heijunka, Kanban, PDCA – each with a PDF report.">
<meta property="og:image" content="{BASE}docs/screenshots/factory.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/logo-static.svg" type="image/svg+xml">
<style>
  :root{{--navy:#14213d;--navy-2:#0b1530;--gold:#f2c94c;--pink:#ef7fb3;--blue:#3b6fd6;--teal:#4fd1c5;--paper:#f6f4ef;--ink:#14213d;--muted:#5c687c;--line:#e3dfd5}}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth}}
  body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Inter,Arial,sans-serif;color:var(--ink);background:var(--paper)}}
  [data-lang="en"] .de,[data-lang="de"] .en{{display:none!important}}
  a{{color:inherit}}
  .hero{{position:relative;overflow:hidden;color:#e9eefb;background:radial-gradient(900px 420px at 85% 0%,rgba(242,201,76,.20),transparent 60%),
    radial-gradient(700px 360px at 0% 100%,rgba(239,127,179,.18),transparent 60%),linear-gradient(135deg,#0b1220,#14213d 55%,#1d2f55)}}
  .hero::before{{content:"";position:absolute;inset:0;opacity:.06;background-image:linear-gradient(#fff 1px,transparent 1px),linear-gradient(90deg,#fff 1px,transparent 1px);background-size:28px 28px;
    -webkit-mask-image:linear-gradient(180deg,#000,transparent);mask-image:linear-gradient(180deg,#000,transparent)}}
  .wrap{{max-width:1180px;margin:0 auto;padding:0 20px;position:relative}}
  .top{{display:flex;align-items:center;gap:12px;padding:18px 0}}
  .top img.wm{{height:48px;width:auto}}
  .langs{{margin-left:auto;display:flex;gap:6px}}
  .langs button{{appearance:none;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);color:#fff;font:600 13px system-ui,sans-serif;padding:6px 11px;border-radius:999px;cursor:pointer}}
  .langs button[aria-pressed="true"]{{background:var(--gold);color:var(--navy);border-color:var(--gold)}}
  .hero-in{{display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:center;padding:26px 0 30px}}
  .kick{{font:700 12px/1 ui-monospace,Menlo,monospace;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}}
  h1{{font-size:clamp(34px,5.4vw,60px);line-height:1.02;margin:14px 0 14px;letter-spacing:-.025em;color:#fff}}
  h1 em{{font-style:normal;background:linear-gradient(90deg,var(--gold),var(--pink));-webkit-background-clip:text;background-clip:text;color:transparent}}
  .lede{{color:#b9c4dc;font-size:17px;line-height:1.6;max-width:600px;margin:0}}
  .cta{{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}}
  .btn{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:700;font-size:15px;border-radius:12px;padding:11px 16px;border:1px solid rgba(255,255,255,.22);color:#fff;background:rgba(255,255,255,.07)}}
  .btn.primary{{background:var(--gold);color:var(--navy);border-color:var(--gold)}}
  .btn:hover{{filter:brightness(1.08)}}
  .facts{{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}}
  .facts span{{font-size:12.5px;font-weight:600;color:#dbe3f3;border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:5px 11px;background:rgba(255,255,255,.05)}}
  .hero-art img{{width:100%;height:auto;display:block;filter:drop-shadow(0 24px 40px rgba(0,0,0,.35))}}
  .steps{{list-style:none;display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin:0;padding:0 0 30px;counter-reset:s}}
  .steps a{{display:block;text-decoration:none;color:#fff;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:12px 12px 11px;position:relative;transition:background .2s,transform .2s}}
  .steps a:hover{{background:rgba(242,201,76,.14);transform:translateY(-2px)}}
  .steps li:not(:last-child) a::after{{content:"›";position:absolute;right:-9px;top:50%;transform:translateY(-50%);color:var(--gold);font-weight:800;z-index:1}}
  .steps i{{font-style:normal;width:24px;height:24px;border-radius:50%;display:inline-grid;place-items:center;background:var(--gold);color:var(--navy);font-weight:900;font-size:13px}}
  .steps b{{display:block;margin-top:8px;font-size:14.5px}}
  .steps small{{color:#9aa8c4;font-size:12px}}
  main{{padding:34px 0 10px}}
  .intro{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:24px}}
  .intro div{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px}}
  .intro b{{display:block;font-size:15px;margin-bottom:4px}}
  .intro p{{margin:0;color:var(--muted);font-size:14px;line-height:1.5}}
  .phase{{margin:34px 0;scroll-margin-top:16px}}
  .ph-head{{display:flex;align-items:center;gap:14px;margin-bottom:14px;border-bottom:1px solid var(--line);padding-bottom:12px}}
  .ph-n{{width:42px;height:42px;border-radius:12px;background:var(--navy);color:var(--gold);display:grid;place-items:center;font-weight:900;font-size:20px;flex:none}}
  .ph-head h2{{margin:0;font-size:24px;letter-spacing:-.01em}}
  .ph-head .q{{margin:2px 0 0;color:var(--muted);font-size:14.5px}}
  .ph-count{{margin-left:auto;font-size:12.5px;font-weight:700;color:var(--muted);white-space:nowrap}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}}
  .card{{position:relative;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column;transition:transform .2s,box-shadow .2s,border-color .2s}}
  .card:hover{{transform:translateY(-3px);box-shadow:0 18px 36px -22px rgba(20,33,61,.45);border-color:#c9c2b2}}
  .card .hit{{position:absolute;inset:0;z-index:1}}
  .card .art{{background:linear-gradient(180deg,#f9f7f2,#f1eee6);padding:10px 14px 4px;aspect-ratio:480/300}}
  .card .art img{{width:100%;height:100%;display:block}}
  .cb{{padding:14px 16px 16px;display:flex;flex-direction:column;flex:1}}
  .cb h3{{margin:0 0 6px;font-size:17px}}
  .cb p{{margin:0 0 12px;color:var(--muted);font-size:14px;line-height:1.5;flex:1}}
  .meta{{display:flex;align-items:center;gap:6px}}
  .pill{{font-size:11px;font-weight:800;letter-spacing:.04em;border:1px solid var(--line);border-radius:999px;padding:3px 8px;color:var(--muted)}}
  .pill.gold{{background:#fff7d9;border-color:#ecddaa;color:#7a5c0c}}
  .go{{margin-left:auto;font-weight:800;color:var(--blue);font-size:14px}}
  .alt{{position:relative;z-index:2;margin-top:8px;font-size:13px;font-weight:700;color:var(--blue);text-decoration:none}}
  footer{{margin-top:40px;background:var(--navy);color:#b9c4dc;font-size:13.5px;line-height:1.6}}
  footer .wrap{{padding-top:26px;padding-bottom:30px;display:flex;gap:18px;flex-wrap:wrap;align-items:center}}
  footer a{{color:#fff}}
  footer img{{width:40px;height:40px}}
  @media(max-width:980px){{.hero-in{{grid-template-columns:1fr}}.hero-art{{order:-1;max-width:560px}}.steps{{grid-template-columns:repeat(3,1fr)}}.intro{{grid-template-columns:1fr}}}}
  @media(max-width:560px){{.steps{{grid-template-columns:repeat(2,1fr)}}.steps li a::after{{display:none}}.top img.wm{{height:40px}}}}
</style>
</head>
<body data-lang="en">
<header class="hero">
  <div class="wrap">
    <div class="top">
      <img class="wm" src="assets/logo-wordmark.svg" alt="Lean · CI · Kaizen Toolkit" width="195" height="48">
      <div class="langs" role="group" aria-label="Language / Sprache">
        <button type="button" data-set="en" aria-pressed="true">🇬🇧 English</button>
        <button type="button" data-set="de" aria-pressed="false">🇩🇪 Deutsch</button>
      </div>
    </div>
    <div class="hero-in">
      <div>
        <div class="kick">{bi("Lean · Six Sigma · Kaizen · CI", "Lean · Six Sigma · Kaizen · KVP")}</div>
        <h1>{bi("Improve any process – ", "Prozesse verbessern – ")}<em>{bi(f"{N_TOOLS} tools, one path.", f"{N_TOOLS} Tools, ein Weg.")}</em></h1>
        <p class="lede">{bi("Free, interactive tools organised along the improvement process: understand the context, define the problem, measure, find the root cause, improve and sustain. Every tool runs in your browser and creates a PDF report for managers and customers.",
                            "Kostenlose, interaktive Werkzeuge entlang des Verbesserungsprozesses: Kontext verstehen, Problem definieren, messen, Ursache finden, verbessern und absichern. Jedes Tool läuft im Browser und erstellt einen PDF-Bericht für Führungskräfte und Kunden.")}</p>
        <div class="cta">
          <a class="btn primary" href="#phase-context">{bi("Start the journey →", "Los geht's →")}</a>
          <a class="btn" href="https://github.com/milad-karami/lean-ci-kaizen-tools" target="_blank" rel="noopener">⭐ GitHub</a>
        </div>
        <div class="facts"><span>{bi("Free", "Kostenlos")}</span><span>{bi("No install", "Ohne Installation")}</span><span>{bi("Works offline", "Läuft offline")}</span><span>{bi("PDF report in every tool", "PDF-Bericht in jedem Tool")}</span><span>{bi("Tools in German · Kanban also in English", "Tools auf Deutsch · Kanban auch auf Englisch")}</span></div>
      </div>
      <div class="hero-art"><img src="assets/illustrations/toolkit-hero.svg" alt="" width="960" height="360"></div>
    </div>
    {stepper()}
  </div>
</header>
<main class="wrap" id="tools">
  <div class="intro">
    <div><b>{bi("1 · Follow the path", "1 · Dem Weg folgen")}</b><p>{bi("The phases follow DMAIC – the Six Sigma improvement cycle – with a strategic context phase in front.", "Die Phasen folgen DMAIC – dem Six-Sigma-Verbesserungszyklus – mit einer vorgeschalteten Kontext-Phase.")}</p></div>
    <div><b>{bi("2 · Work in the tool", "2 · Im Tool arbeiten")}</b><p>{bi("Each tool guides you step by step, with examples, a glossary, FAQ and a quiz. Your work is saved in your browser.", "Jedes Tool führt Schritt für Schritt – mit Beispielen, Glossar, FAQ und Quiz. Deine Arbeit wird im Browser gespeichert.")}</p></div>
    <div><b>{bi("3 · Report the result", "3 · Ergebnis berichten")}</b><p>{bi("Click “Bericht (PDF)” to create a professional report – choose the sections and save it as PDF.", "Klick auf „Bericht (PDF)“ erstellt einen professionellen Bericht – Abschnitte wählen und als PDF sichern.")}</p></div>
  </div>
  {"".join(phase_section(p) for p in CFG["phases"])}
</main>
<footer>
  <div class="wrap">
    <img src="assets/logo.svg" alt="" width="40" height="40">
    <div>
      {bi("Further development:", "Weiterentwicklung:")} <a href="https://www.linkedin.com/in/milad-karami-63075b78/" target="_blank" rel="noopener">Milad Karami</a> ·
      {bi("Original tools: John Naska", "Original-Tools: John Naska")} (<a href="https://www.mokka.solutions/" target="_blank" rel="noopener">mokka.solutions</a>), {bi("published with his permission", "veröffentlicht mit seiner Genehmigung")} ·
      <a href="https://github.com/milad-karami/lean-ci-kaizen-tools" target="_blank" rel="noopener">{bi("Source code & change log on GitHub", "Quellcode & Änderungsprotokoll auf GitHub")}</a>
    </div>
  </div>
</footer>
<script>
(function(){{
  var KEY='leanTools.lang';
  function set(l){{ document.body.dataset.lang=l; document.documentElement.lang=l;
    document.querySelectorAll('.langs button').forEach(function(b){{ b.setAttribute('aria-pressed', String(b.dataset.set===l)); }});
    try{{ localStorage.setItem(KEY,l); }}catch(e){{}} }}
  var saved=null; try{{ saved=localStorage.getItem(KEY); }}catch(e){{}}
  set(saved==='de' ? 'de' : 'en'); // English by default, German as an option
  document.querySelectorAll('.langs button').forEach(function(b){{ b.addEventListener('click',function(){{ set(b.dataset.set); }}); }});
}})();
</script>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print("index.html written:", len(HTML) // 1024, "KB,", N_TOOLS, "tools")
