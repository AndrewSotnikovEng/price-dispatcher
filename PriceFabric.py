import asyncio
import tracemalloc
from Services.ContentService import ContentService
from Parsers.EpikParser import EpikParser
from Parsers.EvaParser import EvaParser
from Parsers.ForaParser import ForaParser
from Model.Good import Good
from Model.GoodDTO import GoodDTO
from Model.Price import Price

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



        
       


