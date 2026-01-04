const express = require('express');
const router = express.Router();

// POST /api/uploads/presigned
router.post('/presigned', async (req, res) => {
  // Placeholder: generate presigned URL (S3/MinIO)
  res.json({ uploadUrl: 'https://example.com/upload' });
});

// POST /api/uploads/complete
router.post('/complete', async (req, res) => {
  // Placeholder: record metadata & enqueue thumbnail job
  res.status(200).json({ ok: true });
});

module.exports = router;
