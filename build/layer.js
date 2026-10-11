/* ===== Lean · CI · Kaizen Toolkit – gemeinsame Ebene: PDF-Bericht für jedes Tool =====
   Der Bericht wird aus dem aktuellen Stand des Tools gebaut (buildMarkdown()), die Abschnitte ergeben sich aus den
   Überschriften des Tools. Druck über ein verstecktes iframe → „Als PDF sichern“. */
(function(){
  'use strict';
  var C = window.TK_CFG; if (!C) return;
  var esc = function(s){ return String(s == null ? '' : s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); };

  /* ---------- Markdown → Blöcke ---------- */
  function inline(t){
    var s = esc(t);
    s = s.replace(/&lt;br\s*\/?&gt;/gi, '<br>');
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/__([^_]+)__/g, '<strong>$1</strong>');
    s = s.replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?!\w)/g, '$1<em>$2</em>');
    s = s.replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2">$1</a>');
    s = s.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, function(_, a, b){ return b || a; });
    s = s.replace(/==([^=]+)==/g, '<mark>$1</mark>');
    return s;
  }
  function parse(md){
    md = String(md || '').replace(/<!--[\s\S]*?-->/g, '').replace(/\r/g, '').replace(/^---\n[\s\S]*?\n---\n/, '');
    var L = md.split('\n'), out = [], i = 0, para = [], m;
    function flush(){ if (para.length){ out.push({t:'p', h:inline(para.join(' '))}); para = []; } }
    var LI = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;
    while (i < L.length){
      var l = L[i];
      if (/^```/.test(l)){ flush(); var lang = l.slice(3).trim(), buf = []; i++;
        while (i < L.length && !/^```/.test(L[i])){ buf.push(L[i]); i++; } i++;
        if (lang !== 'mermaid' && lang !== 'dataview') out.push({t:'pre', h:esc(buf.join('\n'))}); continue; }
      if ((m = l.match(/^(#{1,4})\s+(.*)$/))){ flush(); out.push({t:'h' + m[1].length, text:m[2].replace(/[*_`]/g, '').trim(), h:inline(m[2].trim())}); i++; continue; }
      if (/^\s*\|/.test(l)){ flush(); var rows = [];
        while (i < L.length && /^\s*\|/.test(L[i])){ rows.push(L[i]); i++; }
        var cells = function(r){ return r.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(function(c){ return c.trim(); }); };
        var body = rows.map(cells), head = null;
        if (body.length > 1 && body[1].every(function(c){ return /^:?-{2,}:?$/.test(c); })){ head = body[0]; body = body.slice(2); }
        out.push({t:'table', head:head, body:body}); continue; }
      if (/^\s*>/.test(l)){ flush(); var q = [];
        while (i < L.length && /^\s*>/.test(L[i])){ q.push(L[i].replace(/^\s*>\s?/, '')); i++; }
        var kind = 'note', title = '', c0 = q[0] && q[0].match(/^\[!(\w+)\][-+]?\s*(.*)$/);
        if (c0){ kind = c0[1].toLowerCase(); title = c0[2]; q.shift(); }
        out.push({t:'quote', kind:kind, title:inline(title), h:q.filter(function(x){ return x.trim(); }).map(inline).join('<br>')}); continue; }
      if ((m = l.match(LI))){ flush(); var ordered = /\d/.test(m[2]), items = [];
        while (i < L.length && (m = L[i].match(LI))){
          var txt = m[3], cb = txt.match(/^\[( |x|X)\]\s+(.*)$/);
          if (cb) txt = (cb[1] === ' ' ? '☐ ' : '☑ ') + cb[2];
          items.push({lvl:Math.min(3, Math.floor(m[1].length / 2)), h:inline(txt)}); i++; }
        out.push({t:ordered ? 'ol' : 'ul', items:items}); continue; }
      if (/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(l) || !l.trim()){ flush(); i++; continue; }
      para.push(l.trim()); i++;
    }
    flush(); return out;
  }
  function split(blocks){
    var r = {title:'', intro:[], secs:[]}, cur = null;
    blocks.forEach(function(b){
      if (b.t === 'h1'){ if (!r.title) r.title = b.text; return; }
      if (b.t === 'h2'){ cur = {title:b.text, h:b.h, blocks:[]}; r.secs.push(cur); return; }
      (cur ? cur.blocks : r.intro).push(b);
    });
    return r;
  }
  function html(bs){
    return bs.map(function(b){
      switch (b.t){
        case 'p': return '<p>' + b.h + '</p>';
        case 'h3': return '<h3>' + b.h + '</h3>';
        case 'h4': return '<h4>' + b.h + '</h4>';
        case 'pre': return '<pre>' + b.h + '</pre>';
        case 'quote': return '<div class="callout ' + esc(b.kind) + '">' + (b.title ? '<strong>' + b.title + '</strong>' : '') + (b.h ? '<div>' + b.h + '</div>' : '') + '</div>';
        case 'ul': case 'ol': return '<' + b.t + '>' + b.items.map(function(it){ return '<li class="l' + it.lvl + '">' + it.h + '</li>'; }).join('') + '</' + b.t + '>';
        case 'table': return '<table>' + (b.head ? '<thead><tr>' + b.head.map(function(c){ return '<th>' + inline(c) + '</th>'; }).join('') + '</tr></thead>' : '') +
          '<tbody>' + b.body.map(function(r){ return '<tr>' + r.map(function(c){ return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table>';
        default: return '';
      }
    }).join('');
  }

  /* ---------- Daten aus dem Tool ---------- */
  function getMarkdown(){
    if (typeof window.buildMarkdown !== 'function') throw new Error('Dieses Tool stellt keine Markdown-Ausgabe bereit.');
    var md = window.buildMarkdown();
    if (md && typeof md.then === 'function') throw new Error('Asynchrone Ausgabe wird nicht unterstützt.');
    return String(md || '');
  }
  function glossary(){
    var G = null;
    try { G = (typeof GLOSS !== 'undefined') ? GLOSS : null; } catch (e) { G = null; }
    if (!G || typeof G !== 'object') return [];
    return Object.keys(G).map(function(k){ var v = G[k];
      return v && typeof v === 'object' ? {t:String(v.t || v.title || k), d:String(v.d || v.text || '')} : null; })
      .filter(function(x){ return x && x.t && x.d; });
  }
  function heroText(sel){ var n = document.querySelector('header.hero ' + sel); return n ? n.innerText.replace(/\s+/g, ' ').trim() : ''; }

  /* ---------- Bericht-HTML ---------- */
  var REPORT_CSS = [
    '@page{size:A4;margin:16mm 15mm 18mm;@bottom-left{content:"' + esc(C.title).replace(/"/g, '') + ' · Lean · CI · Kaizen Toolkit";font:7.5pt Arial,sans-serif;color:#6b7280}',
    '@bottom-right{content:"Seite " counter(page) " von " counter(pages);font:7.5pt Arial,sans-serif;color:#6b7280}}',
    '@page cover{margin:0;@bottom-left{content:none}@bottom-right{content:none}}',
    '*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}',
    'html{font-size:10pt}body{margin:0;color:#14213d;font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;line-height:1.5;background:#fff}',
    'h1,h2,h3,h4{font-family:Archivo,system-ui,-apple-system,"Segoe UI",Arial,sans-serif;line-height:1.15;break-after:avoid;page-break-after:avoid;margin:0}',
    '.cover{page:cover;width:210mm;height:297mm;padding:20mm 19mm 16mm;color:#fff;position:relative;overflow:hidden;display:flex;flex-direction:column;break-after:page;',
    'background:radial-gradient(520px 260px at 90% 4%,rgba(242,201,76,.22),transparent 60%),radial-gradient(480px 260px at 0% 100%,rgba(239,127,179,.18),transparent 60%),linear-gradient(140deg,#0b1220,#14213d 55%,#1d2f55)}',
    '.cv-top{display:flex;align-items:center;gap:10px;border-top:2px solid #f2c94c;padding-top:12px;font-size:8.5pt;color:#c8d3e5}',
    '.cv-top svg{width:30px;height:30px}.cv-top b{color:#fff;font-family:Archivo,Arial,sans-serif;font-size:10.5pt}',
    '.cv-top .ph{margin-left:auto;border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:3px 10px;color:#fff}',
    '.cv-main{margin-top:26mm}.cv-kick{color:#f2c94c;font:700 8.5pt "IBM Plex Mono",monospace;letter-spacing:.18em;text-transform:uppercase}',
    '.cv-main h1{font-size:30pt;font-weight:900;letter-spacing:-.02em;margin:10px 0 6px;max-width:165mm}',
    '.cv-main .sub{font-size:14pt;color:#e5ebf5}.cv-meta{margin-top:14px;font-size:10pt;color:#b7c5de}',
    '.cv-for{margin-top:16px;border-left:3px solid #f2c94c;padding-left:12px;max-width:150mm}.cv-for span{display:block;font-size:8pt;color:#b7c5de}.cv-for strong{font-size:12pt}',
    '.cv-art{margin:14mm 0 0;height:70mm;display:flex;justify-content:center}.cv-art svg{height:100%;width:auto;max-width:100%}',
    '.cv-bottom{margin-top:auto;border-top:1px solid #536581;padding-top:10px;display:flex;justify-content:space-between;gap:12px;font-size:8pt;color:#b7c5de}',
    '.cv-bottom b{color:#fff}',
    '.mast{border-bottom:1px solid #e3dfd5;padding-bottom:10px;margin-bottom:6px}.mast .eb{font:700 7.5pt "IBM Plex Mono",monospace;letter-spacing:.16em;text-transform:uppercase;color:#6b7280}',
    '.mast h2{font-size:17pt;margin:5px 0 3px}.mast .meta{display:flex;justify-content:space-between;color:#5c687c;font-size:8.5pt}',
    '.toc{margin:12px 0 4px;padding:10px 12px;background:#f6f4ef;border-radius:8px;break-inside:avoid}.toc h3{font-size:9.5pt;margin-bottom:5px}',
    '.toc ol{margin:0;padding-left:18px;columns:2;column-gap:18px;font-size:8.5pt;color:#374151}',
    '.sec{margin-top:18px}.sec-h{display:flex;gap:10px;align-items:baseline;margin-bottom:8px}.sec-h .no{font:800 10pt Archivo,Arial,sans-serif;color:#9e8644;border-top:3px solid #f2c94c;padding-top:3px;min-width:22px}',
    '.sec-h h2{font-size:14pt;font-weight:800}',
    'p{margin:0 0 7px}h3{font-size:11pt;margin:12px 0 5px}h4{font-size:10pt;margin:10px 0 4px}',
    'ul,ol{margin:0 0 8px;padding-left:18px}li{margin:2px 0}li.l1{margin-left:14px}li.l2{margin-left:28px}li.l3{margin-left:42px}',
    'table{width:100%;border-collapse:collapse;margin:6px 0 10px;font-size:8.8pt}th,td{padding:6px 7px;border-bottom:1px solid #e3dfd5;text-align:left;vertical-align:top}',
    'thead th{background:#f6f4ef;color:#5c687c;font-size:8pt;font-weight:700}tr{break-inside:avoid}',
    '.callout{border:1px solid #e3dfd5;border-left:4px solid #3b6fd6;background:#f4f7fc;border-radius:8px;padding:8px 11px;margin:6px 0 10px;break-inside:avoid}',
    '.callout.tip,.callout.success{border-left-color:#2c6f44;background:#edf7f1}.callout.warning,.callout.danger{border-left-color:#c0563f;background:#fff4f2}',
    '.callout strong{display:block;margin-bottom:2px}code{background:#f1efe8;border-radius:4px;padding:0 4px;font-size:.92em}',
    'pre{background:#f6f4ef;border-radius:8px;padding:8px 10px;font-size:8pt;white-space:pre-wrap;break-inside:avoid}mark{background:#fff0b3}',
    '.note{background:#fff7d9;border:1px solid #ecddaa;border-left:4px solid #f2c94c;border-radius:8px;padding:9px 12px;margin:10px 0;break-inside:avoid;white-space:pre-wrap}',
    '.method{display:flex;gap:14px;align-items:center;background:#f6f4ef;border-radius:10px;padding:12px;break-inside:avoid}',
    '.method svg{width:150px;height:auto;flex:none}.method p{margin:0}',
    '.gloss{columns:2;column-gap:20px;font-size:8.5pt}.gloss div{break-inside:avoid;margin-bottom:7px}.gloss b{display:block}',
    '.cred{font-size:8.8pt;color:#374151;background:#f6f4ef;border-radius:10px;padding:12px;break-inside:avoid}.cred a{color:#315ca9}',
    '@media screen{body{background:#e9ecf1}.page{max-width:210mm;margin:20px auto;background:#fff;padding:16mm 15mm}.cover{margin:20px auto}}',
    '@media print{.new{break-before:page}}'
  ].join('\n');

  function buildReport(o){
    var md = getMarkdown(), doc = split(parse(md));
    var date = new Date().toLocaleDateString('de-DE', {day:'2-digit', month:'long', year:'numeric'});
    var title = C.title, sub = doc.title && doc.title !== C.title ? doc.title : '';
    var chosen = [], n = 0;
    if (o.method) chosen.push(['method', 'Die Methode kurz erklärt']);
    if (o.intro && doc.intro.length) chosen.push(['intro', 'Überblick']);
    doc.secs.forEach(function(s, i){ if (o['s' + i]) chosen.push(['s' + i, s.title]); });
    var gl = glossary();
    if (o.gloss && gl.length) chosen.push(['gloss', 'Begriffe einfach erklärt']);
    if (o.cred) chosen.push(['cred', 'Quellen & Urheberschaft']);
    var body = chosen.map(function(c){
      n++; var id = c[0], inner = '';
      if (id === 'method') inner = '<div class="method">' + (C.art || '') + '<div><p><strong>' + esc(heroText('.kicker')) + '</strong></p><p>' + esc(heroText('p.lede')) + '</p></div></div>';
      else if (id === 'intro') inner = html(doc.intro);
      else if (id === 'gloss') inner = '<div class="gloss">' + gl.map(function(g){ return '<div><b>' + esc(g.t) + '</b>' + esc(g.d) + '</div>'; }).join('') + '</div>';
      else if (id === 'cred') inner = '<div class="cred"><p><strong>Original-Tool:</strong> John Naska (<a href="https://www.mokka.solutions/">mokka.solutions</a>) – veröffentlicht und weiterentwickelt mit seiner Genehmigung.</p>' +
        '<p><strong>Weiterentwicklung (Toolkit):</strong> <a href="https://www.linkedin.com/in/milad-karami-63075b78/">Milad Karami</a> – einheitliches Design, Prozess-Navigation, PDF-Bericht, Fehlerkorrekturen.</p>' +
        '<p><strong>Toolkit:</strong> <a href="https://milad-karami.github.io/lean-ci-kaizen-tools/">milad-karami.github.io/lean-ci-kaizen-tools</a></p>' +
        '<p>Die Inhalte beruhen auf den im Tool verlinkten Quellen (Videos, Kursunterlagen). Die Rechte daran liegen bei den jeweiligen Urheberinnen und Urhebern.</p></div>';
      else { var s = doc.secs[+id.slice(1)]; inner = html(s.blocks); }
      return '<section class="sec"><div class="sec-h"><span class="no">' + String(n).padStart(2, '0') + '</span><h2>' + esc(c[1]) + '</h2></div>' + inner + '</section>';
    }).join('');
    var toc = chosen.length > 2 ? '<div class="toc"><h3>Inhalt</h3><ol>' + chosen.map(function(c){ return '<li>' + esc(c[1]) + '</li>'; }).join('') + '</ol></div>' : '';
    var note = o.note ? '<div class="note"><strong>Anmerkung</strong><br>' + esc(o.note) + '</div>' : '';
    var cover = o.cover ? '<section class="cover"><div class="cv-top">' + (C.logo || '') + '<div><b>Lean · CI · Kaizen</b><br>Toolkit</div><span class="ph">Phase ' + C.phaseN + ' · ' + esc(C.phaseName) + '</span></div>' +
      '<div class="cv-main"><div class="cv-kick">' + esc(heroText('.kicker')) + '</div><h1>' + esc(title) + '</h1>' + (sub ? '<div class="sub">' + esc(sub) + '</div>' : '') +
      '<div class="cv-meta">Bericht vom ' + esc(date) + (o.by ? ' · erstellt von ' + esc(o.by) : '') + '</div>' +
      (o.forWhom ? '<div class="cv-for"><span>Erstellt für</span><strong>' + esc(o.forWhom) + '</strong></div>' : '') + '</div>' +
      '<div class="cv-art">' + (C.art || '') + '</div>' +
      '<div class="cv-bottom"><span>Original-Tool: <b>John Naska</b> (mokka.solutions)</span><span>Toolkit: <b>Milad Karami</b> · milad-karami.github.io/lean-ci-kaizen-tools</span></div></section>' : '';
    var mast = '<header class="mast"><div class="eb">Bericht · Phase ' + C.phaseN + ' · ' + esc(C.phaseName) + '</div><h2>' + esc(title) + '</h2>' +
      '<div class="meta"><span>' + esc(sub || heroText('.kicker')) + '</span><span>' + esc(date) + '</span></div>' +
      (o.forWhom ? '<div class="meta"><span>Erstellt für: <strong>' + esc(o.forWhom) + '</strong></span></div>' : '') + '</header>';
    return '<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>' + esc(title + ' – Bericht – ' + date) + '</title><style>' + REPORT_CSS + '</style></head><body>' +
      cover + '<main class="page">' + mast + toc + note + body + '</main></body></html>';
  }

  /* ---------- Dialog ---------- */
  var KEY = 'tkToolkit.report.v1';
  function load(){ try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } }
  function save(v){ try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} }
  var back = null;
  function openDialog(){
    var doc, err = '';
    try { doc = split(parse(getMarkdown())); } catch (e) { doc = {intro:[], secs:[]}; err = e.message; }
    var gl = glossary(), st = load();
    var opts = [['cover', 'Deckblatt', 'Titel, Phase, Datum, Logo'], ['method', 'Die Methode kurz erklärt', 'Wofür das Werkzeug da ist']];
    if (doc.intro.length) opts.push(['intro', 'Überblick', 'Einleitung aus dem aktuellen Stand']);
    doc.secs.forEach(function(s, i){ opts.push(['s' + i, s.title, 'Inhalt aus dem Tool']); });
    if (gl.length) opts.push(['gloss', 'Begriffe einfach erklärt', gl.length + ' Begriffe']);
    opts.push(['cred', 'Quellen & Urheberschaft', 'Original-Tool, Weiterentwicklung, Quellen']);
    if (!back){
      back = document.createElement('div'); back.className = 'tk-rep-back'; back.setAttribute('role', 'dialog'); back.setAttribute('aria-modal', 'true');
      document.body.appendChild(back);
      back.addEventListener('click', function(e){ if (e.target === back) close(); });
      document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && back.classList.contains('open')) close(); });
    }
    back.innerHTML = '<div class="tk-rep"><div class="tk-rep-head">' + (C.logo || '') + '<div><small>Bericht · Phase ' + C.phaseN + '</small><h2>PDF-Bericht: ' + esc(C.title) + '</h2></div><button class="tk-rep-x" aria-label="Schließen">×</button></div>' +
      '<div class="tk-rep-body"><div class="tk-rep-row"><div><label class="tk-f" for="tkFor">Erstellt für (optional)</label><input id="tkFor" type="text" placeholder="z. B. Geschäftsführung Muster GmbH"></div>' +
      '<div><label class="tk-f" for="tkBy">Erstellt von (optional)</label><input id="tkBy" type="text" placeholder="Ihr Name / Team"></div></div>' +
      '<label class="tk-f" for="tkNote">Anmerkung (optional)</label><textarea id="tkNote" placeholder="z. B. Ziel der Analyse, nächste Schritte …"></textarea>' +
      '<label class="tk-f">Was soll in den Bericht?</label><div class="tk-rep-presets"><button data-p="all">Alles</button><button data-p="res">Nur Ergebnisse</button><button data-p="none">Nichts</button></div>' +
      '<div class="tk-rep-grid">' + opts.map(function(o){ return '<label class="tk-rep-opt"><input type="checkbox" value="' + o[0] + '"' + (o[0] === 'gloss' ? '' : ' checked') + '><span><b>' + esc(o[1]) + '</b><small>' + esc(o[2]) + '</small></span></label>'; }).join('') + '</div>' +
      '<div class="tk-rep-actions"><button class="tk-go">📄 PDF erstellen</button><button class="tk-cancel">Abbrechen</button></div>' +
      (err ? '<div class="tk-rep-err">Hinweis: ' + esc(err) + '</div>' : '') +
      '<div class="tk-rep-hint">Es öffnet sich der Druckdialog – dort <b>„Als PDF sichern“</b> wählen. Der Bericht nutzt den aktuellen Stand dieses Tools.</div></div></div>';
    var q = function(s){ return back.querySelector(s); };
    q('#tkFor').value = st.forWhom || ''; q('#tkBy').value = st.by || '';
    var boxes = Array.prototype.slice.call(back.querySelectorAll('.tk-rep-grid input'));
    back.querySelector('.tk-rep-x').onclick = close; back.querySelector('.tk-cancel').onclick = close;
    back.querySelector('.tk-rep-presets').onclick = function(e){ var p = e.target.getAttribute('data-p'); if (!p) return;
      boxes.forEach(function(b){ b.checked = p === 'all' ? true : p === 'none' ? false : /^(cover|s\d+|intro)$/.test(b.value); }); };
    back.querySelector('.tk-go').onclick = function(){
      var o = {forWhom:q('#tkFor').value.trim(), by:q('#tkBy').value.trim(), note:q('#tkNote').value.trim()};
      boxes.forEach(function(b){ o[b.value] = b.checked; });
      if (!boxes.some(function(b){ return b.checked; })){ alert('Bitte mindestens einen Inhalt auswählen.'); return; }
      save({forWhom:o.forWhom, by:o.by});
      var html;
      try { html = buildReport(o); } catch (e) { alert('Bericht konnte nicht erstellt werden: ' + e.message); return; }
      close(); printHTML(html);
    };
    back.classList.add('open'); setTimeout(function(){ q('#tkFor').focus(); }, 30);
  }
  function close(){ if (back) back.classList.remove('open'); }
  function printHTML(html){
    var old = document.getElementById('tkRepFrame'); if (old) old.remove();
    var f = document.createElement('iframe'); f.id = 'tkRepFrame'; f.setAttribute('aria-hidden', 'true');
    f.style.cssText = 'position:fixed;right:0;bottom:0;width:0;height:0;border:0;visibility:hidden';
    document.body.appendChild(f);
    var d = f.contentDocument; d.open(); d.write(html); d.close();
    var done = false, t0 = document.title;
    var go = function(){ if (done) return; done = true; document.title = d.title || t0; f.contentWindow.focus(); f.contentWindow.print(); setTimeout(function(){ document.title = t0; }, 1000); };
    setTimeout(go, 400);
  }

  /* ---------- Einbau in das Tool ---------- */
  function mount(){
    if (C.noReport) return;
    var ha = document.querySelector('header.hero .hero-actions');
    if (ha && !ha.querySelector('.tk-rep-btn')){
      var b = document.createElement('button'); b.type = 'button'; b.className = 'btn tk-rep-btn'; b.textContent = '📄 Bericht (PDF)';
      b.title = 'Professioneller PDF-Bericht aus dem aktuellen Stand – Inhalte wählbar';
      b.addEventListener('click', openDialog); ha.insertBefore(b, ha.firstChild ? ha.firstChild.nextSibling : null);
    }
    var fm = document.getElementById('fileMenu');
    if (fm && !fm.querySelector('.tk-rep-item')){
      var it = document.createElement('button'); it.className = 'menu-item tk-rep-item'; it.setAttribute('role', 'menuitem');
      it.innerHTML = '<span class="lbl">Als PDF-Bericht …<span class="desc">Für Führungskräfte &amp; Kunden, Inhalte wählbar</span></span>';
      it.addEventListener('click', function(){ fm.hidden = true; openDialog(); });
      var cap = Array.prototype.slice.call(fm.querySelectorAll('.menu-cap')).pop();
      if (cap && cap.nextSibling) fm.insertBefore(it, cap.nextSibling); else fm.appendChild(it);
    }
  }
  window.TK_REPORT = {open:openDialog, build:buildReport, parse:parse};
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
