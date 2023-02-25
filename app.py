from flask import Flask
from fruitDB import FruitDB
app = Flask(__name__)
db = FruitDB()
@app.route('/')
def home():
    fruits = db.all()
    html ='<html>'
    html += '<head><title>Fruit</title></head>'
    html += '<body>'
    html += '<h1>Fruit</h1>'
    html += '<ul>'
    for fruit in fruits:
        html += f'<li>{fruit["fruit"]}  costs {fruit["price"]}</li>'
    html += '</ul>'
    html += '</body>'
    html += '</html>'
    return html


if __name__ == '__main__':
    app.run(debug=True)