from item import Item
from prices_api import get_mappings

class Catalog:
    def __init__(self):
        self.mappings = get_mappings()
        self.items = self.get_items()
        
    def get_items(self):
        return {json['id']: Item(json) for json in self.mappings}
    
    def search_by_name(self, search_name):
        found_items = [item for item in self.items.values() if search_name.lower() in item.name.lower()]
        return found_items
    
if __name__ == '__main__':
    c = Catalog()
    # {print(i) for i in c.items.values()}
    # print(c.items[24393].get_price_info())
    print(c.search_by_name('gold'))