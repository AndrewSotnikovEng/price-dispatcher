from Parsers.BaseParser import BaseParser
import re
class ForaParser(BaseParser):

    def __init__(self):
        super().__init__()

    async def get_product_price(self, browser, url):
        page = await browser.newPage()
        await page.goto(url)

        # Wait for the specific element to be visible
        await page.waitForSelector('div.current-price')

        # Extract the value using page.evaluate
        product_price = await page.evaluate(
            '() => document.querySelector("div.current-price").innerText'
        )

        product_price = self.format_product_price(product_price)

        return product_price


    def format_product_price(self, product_price):
        # For the first case, if it contains three '\n', truncate everything with the second '\n' and replace '\n' with ','
        if product_price.count('\n') == 3:
            last_part = product_price.split('\n', 2)[-1]
            
            # Use a regular expression to capture both parts separately
            matches = re.findall(r'(\d+\.\d+|\d+)', last_part)
            
            if len(matches) >= 2:
                formatted_price = f"{matches[0].replace('.', ',')},{matches[1].replace('.', ',')}"
            else:
                formatted_price = "Price not found"

        # For the second case, if it contains one '\n', replace '\n' with ',' and truncate ' грн'
        elif product_price.count('\n') == 1:
            formatted_price = product_price.replace('\n', ',').replace(' грн', '')

        # If neither case matches, use the entire input
        else:
            formatted_price = product_price

        return formatted_price
