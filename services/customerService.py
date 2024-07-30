from database import db
from models.customer import Customer
from models.product import Product
from sqlalchemy import select
from werkzeug.security import check_password_hash, generate_password_hash
from utils.util import encode_token

def login(username, password):
    query = select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalar_one_or_none()

    if customer and check_password_hash(customer.password, password):
        auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": auth_token
        }
        return response
    else:
        return {
            "status": "error",
            "message": "Invalid username or password"
        }, 401

def save(customer_data):
    hashed_password = generate_password_hash(customer_data['password'])

    new_customer = Customer(
        name=customer_data['name'],
        email=customer_data['email'],
        password=hashed_password,
        phone=customer_data['phone'],
        username=customer_data['username'],
        role_id=customer_data['role_id']
    )
    
    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    query = select(Customer)
    customers = db.paginate(query, page=page, per_page=per_page)
    return customers

def add_to_cart(customer_id, product_id):
    # Checking if the customer exists
    customer_query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(customer_query).scalar_one_or_none()

    if not customer:
        return {"status": "error", "message": "Customer not found"}, 404

    # Checking if the product exists
    product_query = select(Product).where(Product.id == product_id)
    product = db.session.execute(product_query).scalar_one_or_none()

    if not product:
        return {"status": "error", "message": "Product not found"}, 404

    # Adding product to the customer's cart
    if product not in customer.cart:
        customer.cart.append(product)
        db.session.commit()
        return {"status": "success", "message": "Product added to cart"}, 200
    else:
        return {"status": "info", "message": "Product already in cart"}, 200

def remove_from_cart(customer_id, product_id):
    # Checking if the customer exists
    customer_query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(customer_query).scalar_one_or_none()

    if not customer:
        return {"status": "error", "message": "Customer not found"}, 404

    # Checking if the product exists in the cart
    product_query = select(Product).where(Product.id == product_id)
    product = db.session.execute(product_query).scalar_one_or_none()

    if product in customer.cart:
        customer.cart.remove(product)
        db.session.commit()
        return {"status": "success", "message": "Product removed from cart"}, 200
    else:
        return {"status": "info", "message": "Product not found in cart"}, 200

def get_cart(customer_id):
    # Checking if the customer exists
    customer_query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(customer_query).scalar_one_or_none()

    if not customer:
        return {"status": "error", "message": "Customer not found"}, 404

    # Retrieving the customer's cart
    return {
        "status": "success",
        "cart": [product.id for product in customer.cart]
    }, 200
