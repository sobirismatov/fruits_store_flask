import tinydb

class FruitDB:
    def __init__(self):
        self.db = tinydb.TinyDB('fruitDB.json',indent=4, separators=(',', ': '))
        self.table = self.db.table('fruit')

    def add(self, fruit, price):
        self.table.insert({'fruit': fruit, 'price': price})

    def all(self):
        return self.table.all()
    



