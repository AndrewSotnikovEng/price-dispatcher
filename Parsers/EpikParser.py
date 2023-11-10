from Parsers.BaseParser import BaseParser
import re
class EpikParser(BaseParser):

    def __init__(self):
        super().__init__()

    async def get_product_price(self,browser, url):
        page = await browser.newPage()
        await page.goto(url)

        # Wait for the specific element to be visible
        await page.waitForSelector('div.p-price__main')

        # Extract the value using page.evaluate
        product_price = await page.evaluate(
            '() => document.querySelector("div.p-price__main").innerText'
        )

        await page.close()

        formatted_price = self.format_product_price(product_price)

        return formatted_price

    def format_product_price(self, product_price):
        formatted_price = product_price.replace(" ", "")

        return formatted_price

