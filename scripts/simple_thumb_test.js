const fs = require('fs');
const path = require('path');
(async () => {
  try {
    // ensure module resolution finds backend/node_modules
    process.chdir(path.resolve(__dirname, '..', 'backend'));
    const localStore = path.resolve(__dirname, '..', 'local_s3');
    const key = 'uploads/test-sample.jpg';
    const src = path.join(localStore, key);
    if (!fs.existsSync(path.dirname(src))) fs.mkdirSync(path.dirname(src), { recursive: true });
    // write sample if missing
    if (!fs.existsSync(src)) {
      const jpgBase64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQMBAT8A/8QAFBEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPwA//8QAGxAAAgEFAAAAAAAAAAAAAAAAAQIAAwQhQbH/2gAIAQEAAT8hS3YgC8Tx6mJmIln//aAAwDAQACAAMAAAAQ/wD/xAAVEQEBAAAAAAAAAAAAAAAAAAARIf/aAAgBAwEBPxA//8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAgBAgEBPxA//9k=';
      fs.writeFileSync(src, Buffer.from(jpgBase64, 'base64'));
      console.log('Wrote sample', src);
    } else {
      console.log('Sample exists', src);
    }
    const Jimp = require(path.resolve(__dirname, '..', 'backend', 'node_modules', 'jimp'));
    console.log('Jimp export type', typeof Jimp, 'keys', Object.keys(Jimp));
    const start = Date.now();
    const readFn = Jimp.read || (Jimp.default && Jimp.default.read) || (Jimp.Jimp && Jimp.Jimp.read);
    if (!readFn) throw new Error('Jimp.read not found');
    const img = await readFn(src);
    if (img.contain) img.contain(200, 200);
    const thumbKey = key.replace(/(\.[^/.]+)$/, '-thumb$1');
    const dest = path.join(localStore, thumbKey);
    if (img.quality) await img.quality(80).writeAsync(dest);
    else if (img.getBuffer) await img.getBufferAsync(Jimp.MIME_JPEG, (err, buf) => fs.writeFileSync(dest, buf));
    const elapsed = Date.now() - start;
    console.log('Thumb written', dest, 'elapsedMs', elapsed, 'OK<=60000?', elapsed <= 60000);
  } catch (e) {
    console.error('Error', e);
  }
})();
