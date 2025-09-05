const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('http://m.home', { waitUntil: 'networkidle2' });

  // Wait for the data usage elements to appear
  await page.waitForSelector('.used-data');

  // Extract the data usage value (integral, fractional, unit)
  const remaining = await page.evaluate(() => {
    const integral = document.querySelector('.used-data')?.innerText || '';
    const fractional = document.querySelector('.used-data-fractional')?.innerText || '';
    const unit = document.querySelector('.used-data-unit')?.innerText || '';
    return `${integral}${fractional} ${unit}`.trim();
  });

  console.log('Remaining GB:', remaining);

  await browser.close();
})();