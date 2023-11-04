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

    await page.setExtraHTTPHeaders(custom_headers)
    await page.goto(url)
    
    try:
        # Try to find the product price with ins.sf-price__special selector
        await page.waitForSelector('.sf-price ins.sf-price__special')
        product_price = await page.evaluate(
            '() => document.querySelector("ins.sf-price__special").innerText'
        )
    except:
        # If ins.sf-price__special is not found, look for span.sf-price__regular
        await page.waitForSelector('.sf-price span.sf-price__regular')
        product_price = await page.evaluate(
            '() => document.querySelector("span.sf-price__regular").innerText'
        )

    product_price = format_product_price(product_price)
    return product_price




def format_product_price(product_price):
    # For the first case, if it contains three '\n', truncate everything with the second '\n' and replace '\n' with ','
    formatted_price = product_price.replace(' грн', '')

    return formatted_price




async def main():
   
    executable_path = "C:\\Users\\a.sotnikov\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\Local\\pyppeteer\\pyppeteer\\local-chromium\\588429\\chrome-win\\chrome.exe"
    browser = await launch(headless=True, executablePath=executable_path)

    

    urls = [
            "https://eva.ua/ua/pr551247/",
            "https://eva.ua/ua/pr319152/",
            "https://eva.ua/ua/pr702936/",
            "https://eva.ua/ua/pr12292/"

        # Add more URLs as needed
    ]

    for url in urls:
        product_price = await get_product_price(browser, url)
        print(f"{product_price}")

    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())