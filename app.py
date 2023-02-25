from flask import Flask
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    pass


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    pass


# view all grocery by type
@app.route('/grocery/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    pass


# view all grocery by name
@app.route('/grocery/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    pass


# view all grocery by price
@app.route('/grocery/<price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    pass



if __name__ == '__main__':
    app.run(debug=True)