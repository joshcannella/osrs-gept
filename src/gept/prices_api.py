import json
import urllib.request

from constants import MAPPING_URL, PRICES_URL, VOLUMES_URL
    
def _fetch_json(url):
    headers = {
        "User-Agent" : "GE Price Tracker CLI - josh.cannella@yahoo.com"
    }

    req = urllib.request.Request(url, headers=headers)
    f = urllib.request.urlopen(req)
    return json.load(f)

def get_mappings() -> list:
    return _fetch_json(MAPPING_URL)
    
def get_prices() -> dict:
    return _fetch_json(PRICES_URL)['data']

def get_volumes() -> dict:
    return _fetch_json(VOLUMES_URL)['data']

def get_price_by_id(id):
    try:
        return get_prices()[str(id)]
    except KeyError:
        return None
    
def get_volume_by_id(id):
    try:
        return get_volumes()[str(id)]
    except KeyError:
        return None