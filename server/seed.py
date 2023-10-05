from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Pizza, Topping, Order, pizza_toppings
from sqlalchemy.exc import IntegrityError
from faker import Faker

app = Flask(__name__)

# Configuring APP
app.config['SECRET_KEY'] = '19902022'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

fake = Faker()

# Importing models
from models import User, Pizza, Topping, Order

def create_fake_users(num_users=10):
    with app.app_context():
        for _ in range(num_users):
            username = fake.user_name()
            password = fake.password()
            user = User(username=username, password=password)

            db.session.add(user)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

def create_fake_pizzas(num_pizzas=10):
    with app.app_context():
        for _ in range(num_pizzas):
            name = fake.word()
            description = fake.sentence()
            price = fake.random_int(5, 20)
            pizza = Pizza(name=name, description=description, price=price)

            db.session.add(pizza)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

def create_fake_toppings(num_toppings=10):
    with app.app_context():
        for _ in range(num_toppings):
            name = fake.word()
            topping = Topping(name=name)

            db.session.add(topping)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

def create_fake_orders(num_orders=10):
    with app.app_context():
        for _ in range(num_orders):
            user_id = fake.random_int(1, User.query.count())
            order_date = fake.date_time_this_decade()
            total_amount = fake.random_int(10, 100)
            order = Order(user_id=user_id, order_date=order_date, total_amount=total_amount)

            db.session.add(order)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

if __name__ == '__main__':
    create_fake_users()
    create_fake_pizzas()
    create_fake_toppings()
    create_fake_orders()
