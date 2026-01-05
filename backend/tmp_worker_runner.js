const fs = require('fs');
const path = require('path');
fs.appendFileSync(path.resolve(__dirname, '..', 'backend_tmp_worker.log'), 'start\n');
try {
  require('ts-node').register({ transpileOnly: true, require: ['tsconfig-paths/register'] });
  const worker = require('./src/uploads/worker');
  const localStore = path.resolve(__dirname, 'local_s3');
  const key = 'uploads/test-sample.jpg';
  const dest = path.join(localStore, key);
  if (!fs.existsSync(path.dirname(dest))) fs.mkdirSync(path.dirname(dest), { recursive: true });
  const jpgBase64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQMBAT8A/8QAFBEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPwA//8QAGxAAAgEFAAAAAAAAAAAAAAAAAQIAAwQhQbH/2gAIAQEAAT8hS3YgC8Tx6mJmIln//aAAwDAQACAAMAAAAQ/wD/xAAVEQEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPxA//9k=';
  fs.writeFileSync(dest, Buffer.from(jpgBase64, 'base64'));
  fs.appendFileSync(path.resolve(__dirname, '..', 'backend_tmp_worker.log'), 'Wrote ' + dest + '\n');
  worker.processImage('uploads/test-sample.jpg').then(r => {
    fs.appendFileSync(path.resolve(__dirname, '..', 'backend_tmp_worker.log'), 'Worker result: ' + JSON.stringify(r) + '\n');
  }).catch(e => {
    fs.appendFileSync(path.resolve(__dirname, '..', 'backend_tmp_worker.log'), 'Worker error: ' + e + '\n');
  });
} catch (e) {
  fs.appendFileSync(path.resolve(__dirname, '..', 'backend_tmp_worker.log'), 'Exception: ' + e + '\n');
}
