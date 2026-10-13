// usage: node cdp.mjs <file.html> <test.js|-> [shotPath|-] [selector]
// Loads the page in headless Chrome, evaluates test.js (an expression, may be an async IIFE), prints the result and
// "ERRORS: none" or the list of console errors / exceptions.
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
const CHROME = process.env.HOME + '/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell';
const [file, testFile, shot, sel = 'body'] = process.argv.slice(2);
const port = 9300 + Math.floor(Math.random() * 600);
const proc = spawn(CHROME, [`--remote-debugging-port=${port}`, '--window-size=1385,900', '--allow-file-access-from-files', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ws;
for (let i = 0; i < 50; i++) { try { const l = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); const p = l.find(x => x.type === 'page'); if (p) { ws = new WebSocket(p.webSocketDebuggerUrl); break; } } catch {} await sleep(200); }
await new Promise(r => ws.onopen = r);
let id = 0; const pend = {}; const errs = [];
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend[m.id]) { pend[m.id](m); delete pend[m.id]; }
  if (m.method === 'Runtime.exceptionThrown') errs.push('EXC ' + JSON.stringify(m.params.exceptionDetails).slice(0, 400));
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') errs.push('CONSOLE ' + m.params.args.map(a => a.value ?? a.description).join(' ').slice(0, 300)); };
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
await send('Runtime.enable'); await send('Page.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'no-preference' }] });
await send('Page.navigate', { url: 'file://' + resolve(file) }); await sleep(2500);
if (testFile && testFile !== '-') {
  const r = await send('Runtime.evaluate', { expression: readFileSync(testFile, 'utf8'), awaitPromise: true, returnByValue: true });
  if (r.result.exceptionDetails) errs.push('TEST ' + JSON.stringify(r.result.exceptionDetails).slice(0, 400));
  else console.log(JSON.stringify(r.result.result.value, null, 1));
}
if (shot && shot !== '-') {
  const b = await send('Runtime.evaluate', { expression: `(()=>{const s=document.querySelector(${JSON.stringify(sel)});const r=s.getBoundingClientRect();return [r.x+scrollX,r.y+scrollY,r.width,r.height]})()`, returnByValue: true });
  const [x, y, w, h] = b.result.result.value;
  const p = await send('Page.captureScreenshot', { format: 'png', clip: { x, y, width: w, height: h, scale: 1 }, captureBeyondViewport: true });
  writeFileSync(shot, Buffer.from(p.result.data, 'base64'));
}
console.log(errs.length ? 'ERRORS: ' + JSON.stringify(errs, null, 1) : 'ERRORS: none');
ws.close(); proc.kill(); process.exit(0);
