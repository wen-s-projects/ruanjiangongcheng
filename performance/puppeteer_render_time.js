const puppeteer = require('puppeteer');

(async () => {
  const url = process.env.URL || 'http://localhost:3000';
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });
  const perf = JSON.parse(await page.evaluate(() => JSON.stringify(window.performance.timing)));
  // simple metric: domContentLoadedEventEnd - navigationStart
  const dcl = perf.domContentLoadedEventEnd - perf.navigationStart;
  console.log(`dcl=${dcl}`);
  await browser.close();
})();