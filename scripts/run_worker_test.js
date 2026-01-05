const fs = require('fs');
const path = require('path');
const worker = require('../backend/src/uploads/worker');

(async () => {
  const localStore = path.resolve(__dirname, '..', 'backend', 'local_s3');
  const key = 'uploads/test-sample.jpg';
  const dest = path.join(localStore, key);
  if (!fs.existsSync(path.dirname(dest))) fs.mkdirSync(path.dirname(dest), { recursive: true });
  const jpgBase64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQMBAT8A/8QAFBEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPwA//8QAGxAAAgEFAAAAAAAAAAAAAAAAAQIAAwQhQbH/2gAIAQEAAT8hS3YgC8Tx6mJmIln//aAAwDAQACAAMAAAAQ/wD/xAAVEQEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPxA//9k=';
  fs.writeFileSync(dest, Buffer.from(jpgBase64, 'base64'));
  console.log('Wrote', dest);
  try {
    const res = await worker.processImage(key);
    console.log('Worker result:', res);
  } catch (e) {
    console.error('Worker error:', e);
  }
})();
