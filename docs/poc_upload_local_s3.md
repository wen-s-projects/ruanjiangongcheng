# Upload POC (local_s3 fallback)

## Summary

Implemented a local POC for presigned upload + image worker with fallback to `local_s3` when S3/MinIO is unavailable. Integration test and CI workflow were added to validate the worker produces a thumbnail within 60s.

## What I changed

- backend/src/uploads/worker.ts — prefer `local_s3` fast-path; thumbnail generation using `sharp` or `jimp` fallback
- backend/scripts/integration_upload_test.ts — runs `worker.processImage` against `local_s3` sample and validates thumbnail exists and `elapsedMs <= 60000`
- backend/run_worker_sync.js — runner that writes `backend/worker_result.json`
- .github/workflows/upload-poc.yml — CI job to run `npm run test:upload` (on `poc/upload-local-s3` PRs)
- infra/minio/docker-compose.yml — MinIO compose for local e2e
- scripts/presign_e2e.js — script to exercise presign -> PUT -> complete (requires running backend + MinIO)

## Evidence

- Worker run result: `backend/worker_result.json`:

```
{
  "ok": true,
  "result": {
    "thumbKey": "uploads/test-sample-thumb.jpg",
    "elapsedMs": 44
  }
}
```

- Generated thumbnail: `backend/local_s3/uploads/test-sample-thumb.jpg` (size ~460 bytes)

- Integration test: `backend/scripts/integration_upload_test.ts` — `INTEGRATION TEST OK`

## How to reproduce locally

1. Ensure dependencies installed in `backend`: `npm ci`.
2. Make sure `local_s3/uploads/test-sample.jpg` exists (scripts/generate_sample_image.js can generate it).
3. Run `npm run test:upload` in `backend` to run the integration test.
4. To test real S3 flow:
   - Start MinIO: `cd infra/minio && docker compose up -d` (needs Docker)
   - Set env vars in `.env` (S3_ENDPOINT=http://127.0.0.1:9000, S3_BUCKET=mybucket, S3_ACCESS_KEY=minio, S3_SECRET_KEY=minio123)
   - Start backend and run `node scripts/presign_e2e.js`

## Next steps

- Add a CI job that can start MinIO and run full presign e2e (requires runner with Docker support).
- Add additional tests and assertions (e.g., content-type, thumb dimensions).
- Draft PR description and request approval for constitutional exception if needed.

