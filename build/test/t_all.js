(async()=>{const o={};o.bar=!!document.querySelector('.tk-bar');o.art=!!document.querySelector('header.hero > .tk-hero-art img');
o.ver=(document.querySelector('.tk-ver')||{}).textContent||null;
const b=document.querySelector('header.hero .tk-rep-btn'); o.rep=b?b.textContent:null;
if(b&&window.TK_REPORT){try{const x={cover:1,method:1,intro:1,gloss:1,cred:1};for(let i=0;i<40;i++)x['s'+i]=1;o.repKB=Math.round(TK_REPORT.build(x).length/1024);}catch(e){o.repErr=e.message}}
o.lang=document.documentElement.lang;o.langLink=[...document.querySelectorAll('header.hero a[hreflang]')].map(a=>a.getAttribute('href')).join(',');
o.next=(document.querySelector('.tk-next')||{}).getAttribute?.('href');
if(o.lang==='en'){const c=document.body.cloneNode(true);c.querySelectorAll('script,style,template').forEach(e=>e.remove());
 let all=c.textContent;try{all+=buildMarkdown()}catch(e){}
 const re=/.{0,30}\b(?:und|der|die|das|nicht|für|wird|oder|werden|Schritt|Beispiel|Speichern|Bericht)\b.{0,30}/g;
 o.de=[...new Set((all.match(re)||[]).map(s=>s.trim()))].filter(s=>!/Deutsch|Prozessoptimierung|Sehen lernen|einfach erklärt|Geheimtipp|Rüstzeitoptimierung|Projekte leicht|Naska|mokka/.test(s)).slice(0,5);}
return o;})()
