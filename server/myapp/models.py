from myapp import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-orders.user')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    orders = db.relationship('Order', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-toppings.pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    toppings = db.relationship('Topping', secondary='pizza_toppings', back_populates='pizzas', lazy=True)

    def __repr__(self):
        return f'<Pizza {self.name}>'

class Topping(db.Model, SerializerMixin):
    __tablename__ = 'toppings'
    serialize_rules = None

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    pizzas = db.relationship('Pizza', secondary='pizza_toppings', back_populates='toppings', lazy=True)


    def __repr__(self):
        return f'<Topping {self.name}>'

pizza_toppings = db.Table('pizza_toppings',
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True),
    db.Column('topping_id', db.Integer, db.ForeignKey('toppings.id'), primary_key=True)
)



class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    serialize_rules = ('-user.orders',)

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='orders', lazy=True)

    def __repr__(self):
        return f'<Order {self.id}>'
