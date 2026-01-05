const path = require('path');
const fs = require('fs');
(async () => {
  try {
    const sharp = require(path.resolve(__dirname, '..', 'backend', 'node_modules', 'sharp'));
    const outDir = path.resolve(__dirname, '..', 'local_s3', 'uploads');
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
    const out = path.join(outDir, 'test-sample.jpg');
    await sharp({ create: { width: 800, height: 600, channels: 3, background: { r: 220, g: 220, b: 220 } } }).jpeg().toFile(out);
    console.log('Generated sample image', out);
  } catch (e) {
    console.error('Error generating sample image', e);
  }
})();