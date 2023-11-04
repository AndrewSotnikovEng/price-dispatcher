from BaseParser import BaseParser
import re
class EvaParser(BaseParser):

    def __init__(self):
        super().__init__()

    async def get_product_price(self, browser, url):
        custom_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Referer': 'http://www.google.com'
        }
        page = await browser.newPage()

        await page.setExtraHTTPHeaders(custom_headers)
        await page.goto(url)
        
        try:
            # Try to find the product price with ins.sf-price__special selector
            await page.waitForSelector('.sf-price ins.sf-price__special') #possible error plac! Need to be investigated.
            product_price = await page.evaluate(
                '() => document.querySelector("ins.sf-price__special").innerText'
            )
        except:
            # If ins.sf-price__special is not found, look for span.sf-price__regular
            await page.waitForSelector('.sf-price span.sf-price__regular')
            product_price = await page.evaluate(
                '() => document.querySelector("span.sf-price__regular").innerText'
            )

        product_price = self.format_product_price(product_price)
        return product_price




    def format_product_price(self, product_price):
        # For the first case, if it contains three '\n', truncate everything with the second '\n' and replace '\n' with ','
        formatted_price = product_price.replace(' грн', '')
        formatted_price = formatted_price.replace('\xa0', '')

        return formatted_price

