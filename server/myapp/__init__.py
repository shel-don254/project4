from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='23fc56dd8a6b7bc9e2a67f9d36582a7a'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
