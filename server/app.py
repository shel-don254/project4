from flask import jsonify, session, request , render_template
from setup import app, Resource, api, db
from models import Pizza, User, Topping, Order
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")


@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    serialized_users = [user.serialize() for user in users]
    return jsonify(serialized_users)

class Login(Resource):
    def post(self):
        login_data = request.get_json()
        username = login_data.get('username')
        password = login_data.get('password')

        if not username or not password:
            return {"message": "Username and password are required"}, 400
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "User not found"}, 404

        if not user.validate_password(password):
            return {"message": "Invalid password"}, 401
        
        response_data = {
            "message": "Login successful",
            "user_id": user.id
        }
        
        session['user_id'] = user.id
        return response_data, 200 

api.add_resource(Login, '/login', endpoint='login')


class SignUp(Resource):
    def post(self):
        userData = request.get_json()
        username = userData['username']
        password = userData['password']

        new_user = User(username=username)
        new_user.password_hash = password  

        db.session.add(new_user)
        db.session.commit()
        session['random_user'] = new_user.id
        
        response_data = {
            "message": "New user created",
            "user_id": new_user.id
        }
        
        return response_data, 201

api.add_resource(SignUp, '/signup', endpoint='signup')

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


@app.route('/toppings', methods=['GET'])
def list_toppings():
    toppings = Topping.query.all()
    serialized_toppings = [topping.serialize() for topping in toppings]
    return jsonify(serialized_toppings)


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
