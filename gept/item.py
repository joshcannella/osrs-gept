from gept.prices_api import get_price_by_id, get_volume_by_id

class Item:
    def __init__(self, json):
        self.info = json
        self.name = json["name"]
        self.id = json["id"]
        
    def __repr__(self):
        return f"{self.name} ({self.id})"
    
    def get_price_info(self):
        return get_price_by_id(self.id)
    
    def get_volume_info(self):
        return get_volume_by_id(self.id)
    
if __name__ == '__main__':
    item = Item({
        "examine": "It's a bar of gold.",
        "id": 2357,
        "members": False,
        "lowalch": 120,
        "limit": 10000,
        "value": 300,
        "highalch": 180,
        "icon": "Gold bar.png",
        "name": "Gold bar"
    })
    item2 = Item({
        "examine": "A powerful staff.",
        "id": 22647,
        "members": True,
        "lowalch": 120000,
        "limit": 10,
        "value": 300000,
        "highalch": 180000,
        "icon": "Zuriel's staff.png",
        "name": "Zuriel's staff"
    })
    print(item2.get_price_info())
    print(item2.get_volume_info())