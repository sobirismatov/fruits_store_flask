import tinydb

class FruitDB:
    def __init__(self):
        self.db = tinydb.TinyDB('fruitDB.json',indent=4, separators=(',', ': '))
        self.table = self.db.table('fruit')

    def add(self, fruit, price):
        self.table.insert({'fruit': fruit, 'price': price})


# Create a fruit dictionary
fruit ={
    'Apple': 2.4,
    'Orange': 1.2,
    'Banana': 0.5,
    'Tomato': 0.3,
    'Potato': 0.4,
    'Onion': 0.2,
    'Watermelon': 7.3,
    'Cucumber': 0.5,
    'Eggplant': 0.6,
    'Lemon': 0.5,
    'Avocado': 1.2,
    'Apricot': 1.1,
    'Peach': 1.2,
    'Mango': 1.5,
    'Pineapple': 1.3,
    'Blueberry': 1.2,
    'Strawberry': 1.1,
    'Raspberry': 1.2,
    'Cherry': 1.1,
    'Grape': 1.2
}

# Create a FruitDB object
db = FruitDB()

# Add the fruit dictionary to the database
for fruit, price in fruit.items():
    db.add(fruit, price)

        

    