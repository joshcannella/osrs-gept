import json

from gept.item import Item
from gept.prices_api import get_mappings
from gept.utils import normalize_string

class Catalog:
    def __init__(self):
        self.mappings = get_mappings()
        self.items = self.get_items()
        
    def get_items(self):
        return {json['id']: Item(json) for json in self.mappings}
    
    def search_by_name(self, search_name: str) -> list:
        found_items = [item for item in self.items.values() if normalize_string(search_name) in normalize_string(item.name)]
        return found_items
    
def get_item_names():
    file_path = 'items.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    return[item['name'] for item in data]
    
if __name__ == '__main__':
    c = Catalog()
    print(c.search_by_name('gold bar'))