from flask import Flask
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    pass


# view all grocery by type
@app.route('/grocery/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    pass


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    pass


if __name__ == '__main__':
    app.run(debug=True)