import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

export let errorRate = new Rate('errors');

export let options = {
  stages: [
    { duration: '30s', target: 100 }, // ramp to 100 virtual users
    { duration: '1m', target: 100 },
    { duration: '30s', target: 0 }
  ],
  thresholds: {
    'http_req_duration': ['p(95)<1000'], // P95 < 1000ms
    'errors': ['rate<0.01']
  }
};

export default function () {
  const params = { headers: { 'Accept': 'application/json' } };
  // sample tag query (adjust to your API)
  const res = http.get(`${__ENV.BASE_URL || 'http://localhost:3000'}/api/articles?tag=nutrition&page=1&size=20`, params);
  const ok = check(res, {
    'status is 200': (r) => r.status === 200,
    'list non-empty or valid': (r) => r.json().hasOwnProperty('message') || r.json().length >= 0
  });
  if (!ok) errorRate.add(1);
  sleep(1);
}