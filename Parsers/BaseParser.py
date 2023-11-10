import asyncio
from datetime import datetime
from debugpy import configure
from pyppeteer import launch
import re
from Services.Configurer import Configurer

from Model.Price import Price

class BaseParser:

    def __init__(self):
        self.goods = []
        self.prices = []    

    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'http://www.google.com'
    }

    # id, name, url, yesterday_price, today_price, last_updated

    counter = 1
    
    async def get_product_price(self, browser, url):
        return None
    
    def getLastPriceId(self):
        return 123

    async def FillPrice(self):
        browser = await launch(headless=True, executablePath=Configurer.GetExecPath())    
        for good in self.goods:
            product_price = await self.get_product_price(browser, good.url)
            # print(f"{product_price}")
            self.prices.append(Price(self.getLastPriceId(), product_price, datetime.now(), good.shopId, good.id))
        # print("==============================================")

        await browser.close()
        return self.prices
