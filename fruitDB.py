import tinydb

class FruitDB:
    def __init__(self):
        self.db = tinydb.TinyDB('fruitDB.json',indent=4, separators=(',', ': '))
        self.table = self.db.table('fruit')

    def add(self, fruit):
        '''Add a fruit to the database
        
        Args:
            fruit (dict): A dictionary containing the fruit name, quantity, price and type
        '''
        self.table.insert(fruit)

    def all(self):
        '''Get all fruits from the database'''
        return self.table.all()
    
    def get_by_type(self, type: str) -> list:
        '''Get all fruits of a specific type from the database
        
        Args:
            type (str): The type of fruit to get
        
        Returns:
            list: A list of fruits of the specified type
        '''
        q = tinydb.Query()
        return self.table.search(q.type == type)
    


# Create grocery list

grocery = [
    {
        'fruit': 'Apple',
        'quantity': 2,
        'price': 2.4,
        'type': 'fruit'
    },
    {
        'fruit': 'Orange',
        'quantity': 3,
        'price': 1.2,
        'type': 'fruit'
    },
    {
        'fruit': 'Banana',
        'quantity': 4,
        'price': 0.5,
        'type': 'fruit'
    },
    {
        'fruit': 'Tomato',
        'quantity': 5,
        'price': 0.3,
        'type': 'vegetable'
    },
    {
        'fruit': 'Potato',
        'quantity': 6,
        'price': 0.4,
        'type': 'vegetable'
    },
    {
        'fruit': 'Onion',
        'quantity': 7,
        'price': 0.2,
        'type': 'vegetable'
    },
    {
        'fruit': 'Watermelon',
        'quantity': 8,
        'price': 7.3,
        'type': 'fruit'
    },
    {
        'fruit': 'Cucumber',
        'quantity': 9,
        'price': 0.5,
        'type': 'vegetable'
    },
    {
        'fruit': 'Eggplant',
        'quantity': 10,
        'price': 0.6,
        'type': 'vegetable'
    },
    {
        'fruit': 'Lemon',
        'quantity': 11,
        'price': 0.5,
        'type': 'fruit'
    },
    {
        'fruit': 'Avocado',
        'quantity': 12,
        'price': 1.2,
        'type': 'fruit'
    },
    {
        'fruit': 'Apricot',
        'quantity': 13,
        'price': 1.1,
        'type': 'fruit'
    },
    {
        'fruit': 'Peach',
        'quantity': 14,
        'price': 1.2,
        'type': 'fruit'
    },
    {
        'fruit': 'Mango',
        'quantity': 15,
        'price': 1.5,
        'type': 'fruit'
    },
    {
        'fruit': 'Pineapple',
        'quantity': 16,
        'price': 1.3,
        'type': 'fruit'
    },
    {
        'fruit': 'Blueberry',
        'quantity': 17,
        'price': 1.2,
        'type': 'fruit'
    },
    {
        'fruit': 'Strawberry',
        'quantity': 18,
        'price': 1.1,
        'type': 'fruit'
    },
    {
        'fruit': 'Raspberry',
        'quantity': 19,
        'price': 1.2,
        'type': 'fruit'
    },
    {
        'fruit': 'Cherry',
        'quantity': 20,
        'price': 1.1,
        'type': 'fruit'
    },
    {
        'fruit': 'Grape',
        'quantity': 21,
        'price': 1.2,
        'type': 'fruit'
    },
]
    


# Create database
db = FruitDB()

