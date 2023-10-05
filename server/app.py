from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Pizza, Topping, Order, pizza_toppings
app = Flask(__name__)

# Configure your Flask app
app.config['SECRET_KEY'] = '19902022'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for SQLAlchemy

# Initialize SQLAlchemy and Migrate
# db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)


