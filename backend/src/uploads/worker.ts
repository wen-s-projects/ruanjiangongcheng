const makeS3Client = require('./s3.client');
const s3 = makeS3Client();
const bucket = process.env.S3_BUCKET;
const fs = require('fs');
const path = require('path');
const localStore = path.resolve(__dirname, '..', '..', 'local_s3');
if (!fs.existsSync(localStore)) fs.mkdirSync(localStore, { recursive: true });

function tryRequire(name: string) {
  try {
    return require(name);
  } catch (e) {
    return null;
  }
}

const sharp = tryRequire('sharp');
const Jimp = tryRequire('jimp');

async function fetchObject(Key: any) {
  // Fast path: prefer local_s3 file if present to avoid contacting S3 in offline POC environments
  const p = path.join(localStore, Key);
  if (fs.existsSync(p)) {
    const buf = fs.readFileSync(p);
    async function* gen() { yield buf; }
    return gen();
  }
  const { GetObjectCommand } = require('@aws-sdk/client-s3');
  try {
    const stream = await s3.send(new GetObjectCommand({ Bucket: bucket, Key }));
    return stream.Body;
  } catch (e) {
    // fallback to local file if it appears during the operation
    if (fs.existsSync(p)) {
      const buf = fs.readFileSync(p);
      async function* gen() { yield buf; }
      return gen();
    }
    throw e;
  }
}

async function uploadObject(Key: any, Body: any, ContentType: any) {
  const { PutObjectCommand } = require('@aws-sdk/client-s3');
  try {
    await s3.send(new PutObjectCommand({ Bucket: bucket, Key, Body, ContentType }));
  } catch (e) {
    const p = path.join(localStore, Key);
    const dir = path.dirname(p);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(p, Buffer.isBuffer(Body) ? Body : Buffer.from(Body));
  }
}

async function processImage(key: any) {
  const start = Date.now();
  console.log('worker: processing', key);
  const bodyStream = await fetchObject(key);
  const chunks: any[] = [];
  for await (const chunk of bodyStream) chunks.push(chunk);
  const input = Buffer.concat(chunks);

  let thumbBuf: Buffer;
  if (sharp) {
    thumbBuf = await sharp(input).resize(200, 200, { fit: 'inside' }).toBuffer();
  } else if (Jimp) {
    const img = await Jimp.read(input);
    img.contain(200, 200);
    thumbBuf = await img.getBufferAsync(Jimp.MIME_JPEG);
  } else {
    throw new Error('no_image_processor');
  }

  const thumbKey = key.replace(/(\.[^/.]+)$/, '-thumb$1');
  await uploadObject(thumbKey, thumbBuf, 'image/jpeg');
  const elapsed = Date.now() - start;
  console.log(`worker: processed ${key} -> ${thumbKey} in ${elapsed}ms`);
  return { thumbKey, elapsedMs: elapsed };
}

module.exports = { processImage };