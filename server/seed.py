from myapp import db, app
from myapp.models import User, Pizza, Topping, Order, pizza_toppings


def populate_database():
    with app.app_context():
        user = User(username='jones', password='password1')
        topping = Topping(name='Cheese')
        pizza = Pizza(name='Margherita', description='Classic margherita pizza', price=10.99)
        order = Order(total_amount=25.99, user_id=1)

        # db.session.add(user)
        # db.session.add(topping)
        # db.session.add(pizza)
        # db.session.add(order)

        # You can commit after adding all the objects
        pizza_topping1 = pizza_toppings.insert().values(pizza_id=1, topping_id=1)
        db.session.execute(pizza_topping1)

        db.session.commit()

        print("Database seeded")


if __name__ == '__main__':
    populate_database()
