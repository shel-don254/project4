from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from setup import db, bcrypt



pizza_toppings = db.Table(
    'pizza_toppings',
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True),
    db.Column('topping_id', db.Integer, db.ForeignKey('toppings.id'), primary_key=True)
)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  

    orders = db.relationship('Order', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }
    
    @hybrid_property
    def password_hash(self):
        return {"message": "You can't view password hashes"}
    
    @password_hash.setter
    def password_hash(self, password):
     
        self.password = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    def validate_password(self, password):
       
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    toppings = db.relationship('Topping', secondary=pizza_toppings, back_populates='pizzas', lazy=True)
    orders = db.relationship('Order', back_populates='pizza', lazy=True)

    def __repr__(self):
        return f'<Pizza {self.name}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }


class Topping(db.Model, SerializerMixin):
    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


    pizzas = db.relationship('Pizza', secondary=pizza_toppings, back_populates='toppings', lazy=True)

    def __repr__(self):
        return f'<Topping {self.name}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='orders')
    pizza = db.relationship('Pizza', back_populates='orders')

    def __repr__(self):
        return f'<Order {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'pizza_id': self.pizza_id,
            'quantity': self.quantity,
        }