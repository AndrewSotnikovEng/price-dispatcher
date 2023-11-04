import asyncio
from ContentService import ContentService
from GoodDTO import GoodDTO
from PriceFabric import PriceFabric


goods = [
        GoodDTO(1, "Бритва Gillette Mach3 Start з касетою + касети 2 шт.", 1, "https://shop.fora.ua/product/brytva-gillette-mach3-start-z-kasetoiu-kasety-2-sht-734957"),
        GoodDTO(1, "Бритва Gillette Mach3 Start з касетою + касети 2 шт.", 2, "https://eva.ua/ua/pr24963/"),
        GoodDTO(1, "Бритва Gillette Mach3 Start з касетою + касети 2 шт.", 3, "https://epicentrk.ua/shop/stanok-dlya-britya-gillette-mach-3-start-3-smennykh-kartridzha.html"),
        GoodDTO(2, "Папір туалетний «Обухів»", 1, "https://shop.fora.ua/product/papir-tualetnyi-obukhiv-24294"),
        GoodDTO(2, "Папір туалетний «Обухів»", 3, "https://epicentrk.ua/shop/tualetnaya-bumaga-obukhov-65-m-bez-gilzy-1-sht.html"),

    ]

fabric = PriceFabric()
asyncio.run(fabric.run_Fora(ContentService.filterByFora(goods)))  # Use asyncio.run to run the main coroutine
asyncio.run(fabric.run_Eva(ContentService.filterByEva(goods)))  # Use asyncio.run to run the main coroutine
asyncio.run(fabric.run_Epik(ContentService.filterByEpik(goods)))  # Use asyncio.run to run the main coroutine

for price in ContentService.showCurrentPriceByGoodId(fabric.prices, 2, 'asc'):
    print(price)
