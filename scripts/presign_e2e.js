const fs = require('fs');
const path = require('path');
const fetch = require('node-fetch');

async function run() {
  const base = process.env.BACKEND_BASE || 'http://127.0.0.1:3000';
  const sample = path.resolve(__dirname, '..', 'local_s3', 'uploads', 'test-sample.jpg');
  if (!fs.existsSync(sample)) throw new Error('sample missing: ' + sample);
  // get presigned
  const presignRes = await fetch(base + '/api/uploads/presigned', { method: 'POST', headers: { 'Content-Type':'application/json' }, body: JSON.stringify({ filename: 'test-sample.jpg', contentType: 'image/jpeg' }) });
  const presign = await presignRes.json();
  if (!presign || !presign.url || !presign.key) throw new Error('presign failed: ' + JSON.stringify(presign));
  const buf = fs.readFileSync(sample);
  // upload via PUT
  const putRes = await fetch(presign.url, { method: 'PUT', headers: { 'Content-Type':'image/jpeg' }, body: buf });
  if (!(putRes.status >= 200 && putRes.status < 300)) throw new Error('upload failed: ' + putRes.status);
  // notify complete
  const compRes = await fetch(base + '/api/uploads/complete', { method: 'POST', headers: { 'Content-Type':'application/json' }, body: JSON.stringify({ key: presign.key }) });
  const comp = await compRes.json();
  console.log('complete result', comp);
}

run().catch(e=>{ console.error(e && e.stack || e); process.exit(1); });