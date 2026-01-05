Calorie Journal - Backend Skeleton

Overview:
- Node.js skeleton for the `1-calorie-journal` feature.
- Minimal endpoints provided as stubs for: articles, uploads (presigned), markdown preview.

Getting started:
- Copy `.env.example` to `.env` and set `DATABASE_URL` and S3 settings.
- Install dependencies: `npm ci` (in `backend/`)
- Run: `npm run start` (development, requires ts-node)

Notes:
- This is a skeleton: implement auth, Prisma client, and workers for image processing.
- See `specs/1-calorie-journal/` for spec, plan, tasks and database schema.
