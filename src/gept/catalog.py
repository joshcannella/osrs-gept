from item import Item
from prices_api import get_mappings

class Catalog:
    def __init__(self):
        self.mappings = get_mappings()
        self.items = self.get_items()
        
    def get_items(self):
        return {json['id']: Item(json) for json in self.mappings}
    
if __name__ == '__main__':
    c = Catalog()
    {print(i) for i in c.items.values()}