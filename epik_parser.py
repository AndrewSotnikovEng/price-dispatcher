import asyncio
from pyppeteer import launch
import tracemalloc

async def get_product_price(browser, url):
    page = await browser.newPage()
    await page.goto(url)

    # Wait for the specific element to be visible
    await page.waitForSelector('div.p-price__main')

    # Extract the value using page.evaluate
    product_price = await page.evaluate(
        '() => document.querySelector("div.p-price__main").innerText'
    )

    await page.close()

    formatted_price = format_product_price(product_price)

    return formatted_price

def format_product_price(product_price):
    formatted_price = product_price.replace(" ", "")

    return formatted_price

async def main():
    # tracemalloc.start()
    executable_path = "C:\\Users\\a.sotnikov\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\Local\\pyppeteer\\pyppeteer\\local-chromium\\588429\\chrome-win\\chrome.exe"
    browser = await launch(headless=True, executablePath=executable_path)

    urls = [
        "https://epicentrk.ua/shop/tualetnaya-bumaga-obukhov-65-m-bez-gilzy-1-sht.html",
        "https://epicentrk.ua/shop/zhidkost-dlya-ruchnogo-mytya-posudy-fairy-sochnyy-limon-1-l.html"
        # Add more URLs as needed
    ]

    tasks = [get_product_price(browser, url) for url in urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
