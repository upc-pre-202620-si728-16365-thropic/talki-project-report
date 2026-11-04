import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import path from 'node:path';

const [outDir, profileDir] = process.argv.slice(2);
mkdirSync(outDir, { recursive: true });

const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--remote-debugging-port=9333',
  `--user-data-dir=${profileDir}`, 'about:blank',
], { stdio: 'ignore' });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let version;
for (let i = 0; i < 40 && !version; i++) {
  try { version = await (await fetch('http://127.0.0.1:9333/json/version')).json(); } catch { await sleep(500); }
}
if (!version) { chrome.kill(); throw new Error('Chrome no respondió'); }

const ws = new WebSocket(version.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0;
const pending = new Map();
const listeners = [];
ws.onmessage = (e) => {
  const m = JSON.parse(e.data);
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  else listeners.forEach((l) => l(m));
};
const send = (method, params = {}, sessionId) =>
  new Promise((res) => { const i = ++id; pending.set(i, res); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });

const shots = [
  ['client-login-web.png', '/login', { width: 1440, height: 900, mobile: false, dpr: 1 }],
  ['client-login-mobile.png', '/login', { width: 390, height: 844, mobile: true, dpr: 2 }],
  ['client-register-web.png', '/register', { width: 1440, height: 900, mobile: false, dpr: 1 }],
  ['client-register-mobile.png', '/register', { width: 390, height: 844, mobile: true, dpr: 2 }],
];

for (const [file, route, v] of shots) {
  const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
  const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
  await send('Page.enable', {}, sessionId);
  await send('Emulation.setDeviceMetricsOverride', { width: v.width, height: v.height, deviceScaleFactor: v.dpr, mobile: v.mobile }, sessionId);
  const loaded = new Promise((r) => listeners.push((m) => { if (m.method === 'Page.loadEventFired' && m.sessionId === sessionId) r(); }));
  await send('Page.navigate', { url: `http://localhost:3000${route}` }, sessionId);
  await loaded;
  await sleep(2500);
  const { result: { data } } = await send('Page.captureScreenshot', { format: 'png' }, sessionId);
  writeFileSync(path.join(outDir, file), Buffer.from(data, 'base64'));
  console.log('guardada', file, `${v.width}x${v.height}@${v.dpr}`);
  await send('Target.closeTarget', { targetId });
}
ws.close();
chrome.kill();
process.exit(0);
