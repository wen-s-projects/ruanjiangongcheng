Performance tests

- `k6_load_test.js`: k6 load test simulating 100 concurrent readers. Run with: `k6 run performance/k6_load_test.js --env BASE_URL=http://localhost:3000`
- `puppeteer_render_time.js`: measure DOMContentLoaded timing using Puppeteer. Run with: `node performance/puppeteer_render_time.js`
- `lighthouse_check.js`: run Lighthouse to get perf scores. Requires Chrome; run with: `node performance/lighthouse_check.js`

Integration:
- These scripts can be integrated into CI pipelines; use thresholds to fail builds on regressions.
- Adjust endpoints and queries based on the final API schema.
