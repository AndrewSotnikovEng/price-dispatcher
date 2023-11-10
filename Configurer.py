import configparser
import json

from GoodDTO import GoodDTO

class Configurer:
    executable_path = None  # Class-level variable to store the executable path
    goods_json_path = "goods.json"

    def __init__(self):
        self.LoadData()

    def LoadData(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        Configurer.executable_path = self.config['Paths']['executable_path']

    @classmethod
    def GetExecPath(cls):
        if cls.executable_path is None:
            cls().LoadData()  # Create an instance if not created already
        return cls.executable_path
    
    @classmethod
    def load_goods_from_json(cls):
        with open(cls.goods_json_path, 'r', encoding='utf-8') as file:
            goods_data = json.load(file)

        goods = []
        for data in goods_data:
            good = GoodDTO(data['id'], data['name'], data['shopId'], data['url'])
            goods.append(good)

        return goods
        