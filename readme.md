# Fruits Web App

## objective

The objective of this project is to create a web app that allows users to view a list of fruits and add new fruits to the list.

## requirements

- [ ] The app should have a home page that displays a list of fruits.
- [ ] The app should have a form that allows users to add new fruits to the list.
- [ ] The app should show a fruits by specifying the fruit type in the URL.

## databsae structure

```json
{
    "grocery": [
        {
            "name": "Apple",
            "quantity": 2,
            "price": 2.4,
            "type": "fruit"
        },
        {
            "name": "Milk",
            "quantity": 1,
            "price": 2.5,
            "type": "dairy"
        },
        {
            "name": "Carrot",
            "quantity": 2,
            "price": 1.5,
            "type": "vegetable"
        }
        
    ]
}
```

we have a grocery list that contains **fruits, vegetables** and **dairy** products. We want to create a web app that allows users to view a list of fruits and add new fruits to the list.


## GroceryDB - database class

for this project we will use a database class to store our data. The database class will have the following methods:

- [ ] `__init__` - the constructor method that will initialize the database class.
- [ ] `add` - a method that will add a new item to the database.
- [ ] `all` - a method that will return all the items in the database.
- [ ] `get_by_type` - a method that will return all the items in the database that match the type specified in the URL.
- [ ] `get_by_name` - a method that will return all the items in the database that match the name specified in the URL.
- [ ] `get_by_price` - a method that will return all the items in the database that match the price specified in the URL.

## Endpoints

- [ ] GET `/grocery` - this endpoint will display a list of fruits.
- [ ] POST `/grocery/add` - this endpoint will display a form that allows users to add new fruits to the list.
- [ ] GET `/grocery/<type>` - this endpoint will display a list of fruits by specifying the fruit type in the URL.
- [ ] GET `/grocery/<name>` - this endpoint will display a list of fruits by specifying the fruit name in the URL.
- [ ] GET `/grocery/<price>` - this endpoint will display a list of fruits by specifying the fruit price in the URL.
