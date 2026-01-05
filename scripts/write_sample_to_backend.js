const fs = require('fs');
const path = require('path');
const local = path.resolve(__dirname, '..', 'backend', 'local_s3', 'uploads');
if (!fs.existsSync(local)) fs.mkdirSync(local, { recursive: true });
const dest = path.join(local, 'test-sample.jpg');
const jpgBase64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQMBAT8A/8QAFBEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPwA//8QAGxAAAgEFAAAAAAAAAAAAAAAAAQIAAwQhQbH/2gAIAQEAAT8hS3YgC8Tx6mJmIln//aAAwDAQACAAMAAAAQ/wD/xAAVEQEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPxA//9k=';
fs.writeFileSync(dest, Buffer.from(jpgBase64, 'base64'));
console.log('Wrote sample to', dest);
