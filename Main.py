import asyncio
from Configurer import Configurer
from ContentService import ContentService
from GoodDTO import GoodDTO
from PriceFabric import PriceFabric


goods = Configurer.load_goods_from_json()

fabric = PriceFabric()
asyncio.run(fabric.run_Fora(ContentService.filterByFora(goods)))
asyncio.run(fabric.run_Eva(ContentService.filterByEva(goods)))  
asyncio.run(fabric.run_Epik(ContentService.filterByEpik(goods)))

for price in ContentService.showCurrentPriceByGoodId(fabric.prices, 2, 'asc'):
    print(price)
