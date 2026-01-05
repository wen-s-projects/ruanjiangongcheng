import * as express from 'express';
const router = express.Router();
const { getSignedUrl } = require('@aws-sdk/s3-request-presigner');
const { PutObjectCommand } = require('@aws-sdk/client-s3');
const createS3Client = require('./s3.client');
const worker = require('./worker');

const s3 = createS3Client();
const bucket = process.env.S3_BUCKET;

// POST /api/uploads/presigned
router.post('/presigned', async (req: any, res: any) => {
  try {
    const { filename, contentType } = req.body;
    if (!filename || !contentType) return res.status(400).json({ error: 'missing_fields' });
    const key = `uploads/${Date.now()}-${filename}`;
    const command = new PutObjectCommand({ Bucket: bucket, Key: key, ContentType: contentType });
    const url = await getSignedUrl(s3, command, { expiresIn: 60 * 10 }); // 10min
    res.json({ url, key });
  } catch (err) {
    console.error('presign error', err);
    res.status(500).json({ error: 'presign_error' });
  }
});

// POST /api/uploads/complete
// Body: { key }
router.post('/complete', async (req: any, res: any) => {
  try {
    const { key } = req.body;
    if (!key) return res.status(400).json({ error: 'missing_key' });
    const result = await worker.processImage(key);
    res.json({ ok: true, result });
  } catch (err) {
    console.error('upload complete error', err);
    res.status(500).json({ error: 'complete_error' });
  }
});

module.exports = router;
