const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

(async () => {
  const url = process.env.URL || 'http://localhost:3000';
  const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] });
  const opts = { port: chrome.port };
  const runnerResult = await lighthouse(url, opts);
  const report = runnerResult.lhr;
  console.log('Lighthouse performance score:', report.categories.performance.score);
  // Example: check first-contentful-paint
  const fcp = report.audits['first-contentful-paint'].numericValue;
  console.log('FCP ms:', fcp);
  await chrome.kill();
})();