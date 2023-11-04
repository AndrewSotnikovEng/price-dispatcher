import asyncio
from ContentService import ContentService
from EpikParser import EpikParser
from EvaParser import EvaParser
from ForaParser import ForaParser
from Good import Good
import tracemalloc
from GoodDTO import GoodDTO

from Price import Price

class PriceFabric:

    prices = []

    async def run_Fora(self, goodsDto):
        tracemalloc.start()
        parser = ForaParser()  # Create an instance of the ForaParser class
        parser.goods = goodsDto
        filledPrices = await parser.FillPrice()  
        self.prices =  self.prices +  filledPrices
        tracemalloc.stop()

    async def run_Eva(self, goodsDto):
        tracemalloc.start()
        parser = EvaParser()  # Create an instance of the ForaParser class
        parser.goods = goodsDto
        filledPrices = await parser.FillPrice()  
        self.prices =  self.prices + filledPrices
        tracemalloc.stop()

    async def run_Epik(self, goodsDto):
        tracemalloc.start()
        parser = EpikParser()  # Create an instance of the ForaParser class
        parser.goods = goodsDto
        filledPrices = await parser.FillPrice()  
        self.prices =  self.prices + filledPrices
        tracemalloc.stop()



        
       


