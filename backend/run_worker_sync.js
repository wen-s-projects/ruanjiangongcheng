const fs = require('fs');
const path = require('path');
try {
  require('ts-node').register({ transpileOnly: true, require: ['tsconfig-paths/register'] });
} catch (e) {
  console.error('ts-node register error', e);
}
(async () => {
  try {
    const worker = require('./src/uploads/worker');
    console.log('Calling worker.processImage');
    const res = await worker.processImage('uploads/test-sample.jpg');
    console.log('WORKER RESULT', res);
    const outFile = path.resolve(__dirname, 'worker_result.json');
    fs.writeFileSync(outFile, JSON.stringify({ ok: true, result: res }, null, 2));
    console.log('Wrote result to', outFile);
  } catch (err) {
    console.error('WORKER ERROR', err && (err.stack || err));
    try { fs.writeFileSync(path.resolve(__dirname, 'worker_error.log'), String(err && (err.stack || err))); } catch (e) {}
  }
})();
