import asyncio
from pyppeteer import launch
import re

async def get_product_price(browser, url):
    custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Referer': 'http://www.google.com'
    }
    page = await browser.newPage()
    await page.goto(url)
    
    # Wait for the specific element to be visible
    await page.waitForSelector('div.current-price')

    # Extract the value using page.evaluate
    product_price = await page.evaluate(
        '() => document.querySelector("div.current-price").innerText'
    )

    product_price = format_product_price(product_price)

    return product_price

import re

def format_product_price(product_price):
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




async def main():
    executable_path = "C:\\Users\\a.sotnikov\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\Local\\pyppeteer\\pyppeteer\\local-chromium\\588429\\chrome-win\\chrome.exe"
    browser = await launch(headless=True, executablePath=executable_path)

    urls = [
            "https://shop.fora.ua/product/napii-na-osnovi-vyna-latinium-sparkling-bilyi-napivsukhyi-757558?index=2&list=fora-recommends/main_page",
            "https://shop.fora.ua/product/shokolad-kinder-t8-29055",
            "https://shop.fora.ua/product/papir-tualetnyi-grite-perlum-3-sharovyi-932260?index=2&list=laik_tsina/set_page",
            "https://shop.fora.ua/product/nektar-jaffa-apelsynovyi-760337?index=4&list=fora-recommends/product_page",
            "https://shop.fora.ua/product/kreida-kolorova-dlia-maliuvannia-842785?index=5&list=all-offers/main_page",
            "https://shop.fora.ua/product/syr-exquisa-vershkovyi-classic-70-712457?index=9&list=laik_tsina/set_page"
        # Add more URLs as needed
    ]

    for url in urls:
        product_price = await get_product_price(browser, url)
        print(f"{product_price}")

    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())