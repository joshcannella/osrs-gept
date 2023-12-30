from prices_api import PricesApi

class Catalog:
    def __init__(self):
        self.__api = PricesApi()
        self.mappings = self.__api.get_mappings()