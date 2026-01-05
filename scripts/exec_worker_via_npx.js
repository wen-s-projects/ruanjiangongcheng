const { spawn } = require('child_process');
const cmd = process.platform === 'win32' ? 'npx.cmd' : 'npx';
const args = ['-y', 'ts-node', '-r', 'tsconfig-paths/register', '-e', `(async ()=>{ const w = await import('../backend/src/uploads/worker'); try{ const r = await w.processImage('uploads/test-sample.jpg'); console.log(JSON.stringify({ok:true,result:r})); } catch(e){ console.error('WORKER_ERR', e && e.stack? e.stack : e);} })()`];
console.log('Spawning', cmd, args.join(' '));
const p = spawn(cmd, args, { stdio: ['ignore', 'pipe', 'pipe'] });
p.stdout.on('data', d => process.stdout.write(d));
p.stderr.on('data', d => process.stderr.write(d));
p.on('close', code => console.log('child exit', code));
