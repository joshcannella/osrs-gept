import json
import urllib.request

from constants import MAPPING_URL, PRICES_URL, VOLUMES_URL

class PricesApi:
    def __init__(self):
        pass
    
    def __fetch_json(self, url):
        headers = {
            "User-Agent" : "GE Price Tracker CLI - josh.cannella@yahoo.com"
        }

        req = urllib.request.Request(url, headers=headers)
        f = urllib.request.urlopen(req)
        return json.load(f)
    
    def get_mappings(self):
        return self.__fetch_json(MAPPING_URL)
    
    def get_prices(self):
        return self.__fetch_json(PRICES_URL)['data']
    
    def get_volumes(self):
        return self.__fetch_json(VOLUMES_URL)['data']