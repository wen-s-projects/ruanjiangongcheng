try {
  require('ts-node').register({ transpileOnly: true, require: ['tsconfig-paths/register'] });
} catch (e) {
  console.error('ts-node register error', e);
}
try {
  const worker = require('./src/uploads/worker');
  (async () => {
    try {
      console.log('Calling worker.processImage');
      const res = await worker.processImage('uploads/test-sample.jpg');
      console.log('WORKER RESULT', res);
    } catch (err) {
      console.error('WORKER ERROR', err);
    }
  })();
} catch (e) {
  console.error('require worker error', e);
}
