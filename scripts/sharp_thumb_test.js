const fs = require('fs');
const path = require('path');
(async () => {
  try {
    const localStore = path.resolve(__dirname, '..', 'local_s3');
    const key = 'uploads/test-sample.jpg';
    const src = path.join(localStore, key);
    if (!fs.existsSync(src)) throw new Error('source missing ' + src);
    const sharp = require(path.resolve(__dirname, '..', 'backend', 'node_modules', 'sharp'));
    const start = Date.now();
    const out = path.join(localStore, key.replace(/(\.[^/.]+)$/, '-thumb$1'));
    await sharp(src).resize(200, 200, { fit: 'inside' }).toFile(out);
    const elapsed = Date.now() - start;
    console.log('Thumb written', out, 'elapsedMs', elapsed, 'OK<=60000?', elapsed <= 60000);
  } catch (e) {
    console.error('Error', e);
  }
})();