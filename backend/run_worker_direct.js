const fs = require('fs');
const path = require('path');
const log = (s) => fs.appendFileSync(path.resolve(__dirname, 'worker_run.log'), s + '\n');
log('start');
try {
  require('ts-node').register({ transpileOnly: true, require: ['tsconfig-paths/register'] });
  const worker = require('./src/uploads/worker');
  const localStore = path.resolve(__dirname, 'local_s3');
  const key = 'uploads/test.jpg';
  const dest = path.join(localStore, key);
  if (!fs.existsSync(path.dirname(dest))) fs.mkdirSync(path.dirname(dest), { recursive: true });
  if (!fs.existsSync(dest)) fs.writeFileSync(dest, 'test');
  log('Wrote sample ' + dest);
  worker.processImage(key).then(r => {
    log('Worker result: ' + JSON.stringify(r));
  }).catch(e => {
    log('Worker error: ' + e);
  });
} catch (e) {
  log('Exception: ' + e);
}
