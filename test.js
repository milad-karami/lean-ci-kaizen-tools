(async()=>{const w=ms=>new Promise(r=>setTimeout(r,ms));
const out={fails:[],ex:{},re:{},ger:{}};
const G=/[äöüÄÖÜß]|\b(und|der|die|das|nicht|mit|für|wird|ist|ein|eine|oder|auf|bei|Sie|du|dein|werden|auch|zum|zur|Analyse|Schritt|Beispiel|Durchlauf|Vorhaben|Karte|erledigt)\b/g;
const scan=(l,t)=>{const m=t.match(G); if(m) out.ger[l]=[...new Set(m)];};
const T=async(n,f)=>{try{await f()}catch(e){out.fails.push(n+': '+e.message)}};
for(const id of Object.keys(EXAMPLES)){
 await T('ex '+id,async()=>{
  dirty=false; loadKey('ex:'+id); await w(60);
  const md=buildMarkdown(),js=buildJSON(),ob=buildObsidian();
  out.ex[id]=[md.length,js.length,ob.length];
  scan(id+':md',md.replace(/<!-- pdca-state.*-->/s,'')); scan(id+':ob',ob.replace(/<!-- pdca-state.*-->/s,'')); scan(id+':json',js);
  const b=JSON.stringify(ensureShape(D));
  out.re[id]=[md,js,ob].map(t=>JSON.stringify(importFromText(t))===b);
  scan(id+':body',document.body.innerText);
  for(const p of ['paneTool']) ;
  el('#focusSwitch').click(); await w(20);
  for(let g=1;g<=WIZ.length;g++){gstep=g;applyGuided();scan(id+':wiz'+g,el('#wizTop').textContent);}
  el('#gDone')&&el('#gDone').click(); scan(id+':done',el('#wizTop').textContent);
  if(guided) el('#focusSwitch').click();
 });
}
await T('faq',async()=>{scan('faq',el('#paneFaq').textContent);scan('gloss',el('#glossBox').textContent);scan('save',el('#saveHelp').textContent);scan('foot',el('.foot').textContent);});
await T('quiz',async()=>{document.querySelector('.vsmtab[data-pane="quiz"]').click();await w(50);scan('qsetup',el('#qzApp').textContent);
 for(const q of QZ_BANK){const x=q.gen?q.make():q;scan('q:'+q.id,[x.q,x.expl,x.hint,...(x.o||[]).map(o=>o.x+' '+o.w),...(x.cats||[]),...(x.items||[]).map(i=>i.x||i)].join(' | '));}
 el('#qzGo').click();await w(30);
 for(let i=0;i<40&&el('#qzQuit');i++){const c=el('#qzCheck');document.querySelector('.qz-opt')&&document.querySelector('.qz-opt').click();el('#qzCheck')&&!el('#qzCheck').disabled&&el('#qzCheck').click();el('#qzReveal')&&el('#qzReveal').click();el('#qzNext')&&el('#qzNext').click();scan('qplay',el('#qzApp').textContent);await w(3);}
 scan('qend',el('#qzApp').textContent);out.bank=QZ_BANK.length;});
await T('modals',async()=>{openModal();scan('proj',el('#projModal').textContent);closeModal();openSaveDialog();scan('save',el('#saveModal').textContent);closeSaveDialog();dirty=false;loadKey('ex:alltag');saveCurrent();doSaveAs();await w(30);openModal();scan('proj2',el('#projModal').textContent);closeModal();scan('rep',el('#reportBox').textContent);newCycle();scan('cyc',document.body.innerText);});
out.ids=document.querySelectorAll('[id]').length;
return out;})()
