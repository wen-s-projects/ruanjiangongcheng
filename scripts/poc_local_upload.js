const fs = require('fs');
const path = require('path');
const http = require('http');

const localStore = path.resolve(__dirname, '..', 'backend', 'local_s3');
const key = 'uploads/test-sample.jpg';
const dest = path.join(localStore, key);

if (!fs.existsSync(path.dirname(dest))) fs.mkdirSync(path.dirname(dest), { recursive: true });
// Small 1x1 white JPEG base64
const jpgBase64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQMBAT8A/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPwA//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQAGPwJ//8QAGxAAAgEFAAAAAAAAAAAAAAAAAQIAAwQhQbH/2gAIAQEAAT8hS3YgC8Tx6mJmIln//aAAwDAQACAAMAAAAQ/wD/xAAVEQEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPxA//9k=';
const buf = Buffer.from(jpgBase64, 'base64');
fs.writeFileSync(dest, buf);
console.log('Wrote local file', dest);

const postData = JSON.stringify({ key });
const options = {
  hostname: '127.0.0.1',
  port: 3000,
  path: '/api/uploads/complete',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(postData),
  },
};

const req = http.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => (data += chunk));
  res.on('end', () => {
    console.log('Response:', data);
    try {
      const j = JSON.parse(data);
      if (j && j.result && typeof j.result.elapsedMs === 'number') {
        console.log('Elapsed ms:', j.result.elapsedMs, 'OK <=60000?', j.result.elapsedMs <= 60000);
      }
    } catch (e) {
      console.error('Invalid JSON response', e);
    }
  });
});

req.on('error', (e) => {
  console.error('Request error', e);
});

req.write(postData);
req.end();
