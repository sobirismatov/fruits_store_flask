from flask import Flask,request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route("/")
def home():
    h=''' 
    <html>
    <head><title>Fruits Web App</title>
    
    </head>

    <body>
    <h1>Fruits Web App</h1>
    
    <ul>
    <li><a href="http://127.0.0.1:5000/grocery/grocery">Grocery</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Type</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/name/apple">Name</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price</a></li>
    </ul>
    </html>
    '''
    return h
@app.route('/grocery/grocery')
def all_grocery():
    """Get all grocery"""
    html='''<!DOCTYPE html>
    <html>
    <head>
    <title>Grocery</title>

    <style>
        table, th, td {
            border: 1px solid rgb(47, 190, 97);
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>
    </head>
    <body>

        <h1>My Grocery List</h1>
        
        <table>
            <tr>
                <th>name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>type</th>
            </tr>
    <ul>
    <li><a href="http://127.0.0.1:5000/grocery/grocery">Grocery</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Type</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/name/apple">Name</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price</a></li>
    </ul>    
    '''  
    for grocery in db.all() :
       html+=f'''
       <tr>
       <td>{grocery["name"]}</td>
       <td>{grocery["quantity"]}</td>
       <td>{grocery["price"]}$</td>
       <td>{grocery["type"]}</td>
       </tr>'''
       
    html+="</table>"
    
    return html


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    data=request.get_json(force=True)
    db.add(data)
    return "qushildi"

# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    html='''<!DOCTYPE html>
    <html>
    <head>
    <title>Grocery</title>

    <style>
        table, th, td {
            border: 1px solid rgb(47, 190, 97);
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>
    </head>
    <body>

        <h1>My Grocery List</h1>
        
        <table>
            <tr>
                <th>name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>type</th>
            </tr> 
    <ul>
    <li><a href="http://127.0.0.1:5000/grocery/grocery">Grocery</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Type</a></li>
       <ol>
       <li><a href="http://127.0.0.1:5000/grocery/type/fruit">fruit</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/type/dairy">dairy</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/type/bakery">bakery</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/type/meat">meat</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/type/grain">grain</a></li>
       </ol>
    <li><a href="http://127.0.0.1:5000/grocery/name/apple">Name</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price</a></li>
    </ul>    
    '''  
    for fruit in db.get_by_type(type=type) :
       html+=f'''
       <tr>
       <td>{fruit["name"]}</td>
       <td>{fruit["quantity"]}</td>
       <td>{fruit["price"]}$</td>
       <td>{fruit["type"]}</td>
       </tr>
       
    '''
       
    html+="</table>"
    return html


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    html='''<!DOCTYPE html>
    <html>
    <head>
    <title>Grocery</title>

    <style>
        table, th, td {
            border: 1px solid rgb(47, 190, 97);
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>
    </head>
    <body>

        <h1>My Grocery List</h1>
        
        <table>
            <tr>
                <th>name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>type</th>
            </tr> 
            <ul>
    <li><a href="http://127.0.0.1:5000/grocery/grocery">Grocery</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruit</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/name/apple">Name</a></li>
       <ol>
       <li><a href="http://127.0.0.1:5000/grocery/name/Chicken">Chicken</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/name/melon">melon</a></li>
       <li><a href="http://127.0.0.1:5000/grocery/name/Tomato">Tomato</a></li>
       </ol>
    <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price</a></li>
    </ul>    
    '''  
    for fruit in db.get_by_name(name=name) :
       html+=f'''
       <tr>
       <td>{fruit["name"]}</td>
       <td>{fruit["quantity"]}</td>
       <td>{fruit["price"]}$</td>
       <td>{fruit["type"]}</td>
       </tr>'''
       
    html+="</table>"
    return html


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    html='''<!DOCTYPE html>
    <html>
    <head>
    <title>Grocery</title>

    <style>
        table, th, td {
            border: 1px solid rgb(47, 190, 97);
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>
    </head>
    <body>

        <h1>My Grocery List</h1>
        
        <table>
            <tr>
                <th>name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>type</th>
            </tr>  
            <ul>
    <li><a href="http://127.0.0.1:5000/grocery/grocery">Grocery</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/type/fruit">Fruit</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/name/apple">Name</a></li>
    <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price</a></li>
      <ol>
      <li><a href="http://127.0.0.1:5000/grocery/price/2.4">price 2.4</a></li>
      <li><a href="http://127.0.0.1:5000/grocery/price/4.8">price 4.8</a></li>
      <li><a href="http://127.0.0.1:5000/grocery/price/2.5">price 2.5</a></li>
      <li><a href="http://127.0.0.1:5000/grocery/price/1.5">price 1.5</a></li>
      </ol<
      
    </ul>   
    '''  
    for fruit in db.get_by_price(price=price) :
       html+=f'''
       <tr>
       <td>{fruit["name"]}</td>
       <td>{fruit["quantity"]}</td>
       <td>{fruit["price"]}$</td>
       <td>{fruit["type"]}</td>
       </tr>'''
       
    html+="</table>"
    return html



if __name__ == '__main__':
    app.run(debug=True)