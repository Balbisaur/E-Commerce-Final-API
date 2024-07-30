from models.order import Order
from datetime import date
from sqlalchemy import select
from database import db
from models.product import Product
from models.customer import Customer

def save(order_data):
    # Creating a new Order instance with today's date and the given customer ID
    new_order = Order(date=date.today(), customer_id=order_data['customer_id'])

    # Iterating over product IDs and add products to the order
    for item_id in order_data['product_ids']:
        query = select(Product).where(Product.id == item_id)
        item = db.session.execute(query).scalar_one_or_none()
        if item:
            new_order.products.append(item)
        else:
            # Handle case where product ID is invalid
            print(f"Product with ID {item_id} not found")

    # Adding and committing the new order
    db.session.add(new_order)
    db.session.commit()
    db.session.refresh(new_order)
    return new_order

def find_all():
    # Retrieving all orders
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_by_id(id):
    # Retrieving orders by ID
    query = select(Order).filter(Order.id == id)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_by_customer_id(id):
    # Retrieving orders by customer ID
    query = select(Order).filter(Order.customer_id == id)
    orders = db.session.execute(query).scalars().all()
    return orders

def find_by_customer_email(email):
    # Retrieving orders by customer email
    query = select(Order).join(Customer).filter(Customer.id == Order.customer_id, Customer.email == email)
    orders = db.session.execute(query).scalars().all()
    return orders
