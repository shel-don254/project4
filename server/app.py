from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Pizza, Topping, Order

app = Flask(__name__)

# Configuring the app
app.config['SECRET_KEY'] = '19902022'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Routes for listing all users
@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    serialized_users = [user.serialize() for user in users]
    return jsonify(serialized_users)

# Route for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# Routes for listing all pizzas and creating a new pizza
@app.route('/pizzas', methods=['GET', 'POST'])
def pizzas():
    if request.method == 'GET':
        pizzas = Pizza.query.all()
        serialized_pizzas = [pizza.serialize() for pizza in pizzas]
        return jsonify(serialized_pizzas)
    elif request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')

        if not name or not price:
            return jsonify({'message': 'Name and price are required'}), 400

        pizza = Pizza(name=name, price=price)
        db.session.add(pizza)
        db.session.commit()

        return jsonify({'message': 'Pizza created successfully'}), 201

# Route for listing all toppings
@app.route('/toppings', methods=['GET'])
def list_toppings():
    toppings = Topping.query.all()
    serialized_toppings = [topping.serialize() for topping in toppings]
    return jsonify(serialized_toppings)

# Route for creating a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    pizza_id = data.get('pizza_id')
    quantity = data.get('quantity')

    if not user_id or not pizza_id or not quantity:
        return jsonify({'message': 'User ID, pizza ID, and quantity are required'}), 400

    user = User.query.get(user_id)
    pizza = Pizza.query.get(pizza_id)

    if not user or not pizza:
        return jsonify({'message': 'User or pizza not found'}), 404

    order = Order(user=user, pizza=pizza, quantity=quantity)
    db.session.add(order)
    db.session.commit()

    return jsonify({'message': 'Order created successfully'}), 201

if __name__ == '__main__':
    app.run()
