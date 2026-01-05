import fs from 'fs';
import path from 'path';

async function main() {
  const localStore = path.resolve(__dirname, '..', 'local_s3');
  const key = 'uploads/test-sample.jpg';
  const src = path.join(localStore, key);
  if (!fs.existsSync(path.dirname(src))) fs.mkdirSync(path.dirname(src), { recursive: true });
  // ensure sample exists (generate via sharp if possible)
  if (!fs.existsSync(src)) {
    try {
      const sharp = require(path.resolve(__dirname, '..', 'node_modules', 'sharp'));
      await sharp({ create: { width: 800, height: 600, channels: 3, background: { r: 240, g: 240, b: 240 } } }).jpeg().toFile(src);
      console.log('Generated sample image', src);
    } catch (e) {
      throw new Error('missing sample and cannot generate: ' + e);
    }
  }

  // require the CommonJS module
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const worker = require('../src/uploads/worker') as any;
  const res = await worker.processImage(key);
  console.log('Worker returned:', res);
  if (!res || typeof res.elapsedMs !== 'number') throw new Error('invalid result');
  if (res.elapsedMs > 60000) throw new Error('elapsedMs > 60000: ' + res.elapsedMs);
  const thumbPath = path.join(localStore, res.thumbKey);
  if (!fs.existsSync(thumbPath)) throw new Error('thumb file missing: ' + thumbPath);
  const stat = fs.statSync(thumbPath);
  console.log('Thumb exists:', thumbPath, 'size', stat.size, 'elapsedMs', res.elapsedMs);
}

main().then(()=>{ console.log('INTEGRATION TEST OK'); process.exit(0); }).catch(e=>{ console.error('INTEGRATION TEST FAILED', e && (e.stack||e)); process.exit(1); });
