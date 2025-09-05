const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('http://m.home/index.html', { waitUntil: 'networkidle2' });

    // Wait for the data usage elements to appear
    await page.waitForSelector('.used-data', { timeout: 15000 });

    // Extract the data usage value (integral, fractional, unit)
    const remaining = await page.evaluate(() => {
      const integral = document.querySelector('.used-data')?.innerText || '';
      const fractional = document.querySelector('.used-data-fractional')?.innerText || '';
      const unit = document.querySelector('.used-data-unit')?.innerText || '';
      return `${integral}${fractional} ${unit}`.trim();
    });

    if (!remaining || remaining === ' ') {
      console.log('DEBUG: Data usage value is blank. Check selectors or page rendering.');
    } else {
      console.log('Remaining GB:', remaining);
    }

    await browser.close();
  } catch (err) {
    console.error('ERROR:', err);
  }
})();