Title: feat(poc): upload POC (local_s3 fallback) — integration test + worker + CI

Summary:
This PR implements the Upload POC with a local fallback (local_s3) and adds an integration test and CI workflow to validate thumbnail generation SLA (<= 60s).

Changes:
- Prefer local_s3 fast path in `backend/src/uploads/worker.ts` when S3 is unavailable
- Add `backend/scripts/integration_upload_test.ts` (integration test for worker)
- Add `backend/run_worker_sync.js` to produce `backend/worker_result.json` from a local worker run
- Add `.github/workflows/upload-poc.yml` to run `backend` `npm run test:upload` on PRs to `poc/upload-local-s3`
- Add `infra/minio/docker-compose.yml` and `scripts/presign_e2e.js` to support local MinIO end-to-end testing
- Add `docs/poc_upload_local_s3.md` with reproduction steps and evidence

How to verify:
1. In `backend`, run `npm ci` then `npm run test:upload` (integration test).
2. To run end-to-end with MinIO: `cd infra/minio && docker compose up -d`, set S3 env in `.env`, start backend, then run `node scripts/presign_e2e.js`.

Notes:
- Attachments: `backend/worker_result.json` and generated `backend/local_s3/uploads/test-sample-thumb.jpg` are included in the branch for review.
- Next steps: Add CI job to spin MinIO (requires Docker in runner) to run true presign e2e, add more assertions (image dimensions, content-type), and add CI gating if desired.
