from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Pizza, Topping, Order, pizza_toppings
app = Flask(__name__)

# Configuring the app
app.config['SECRET_KEY'] = '19902022' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)
migrate = Migrate(app, db)


