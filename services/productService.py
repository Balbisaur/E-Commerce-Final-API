from models.product import Product
from database import db
from sqlalchemy import select

def save(product_data):
    # I am creating a new Product instance with the provided data
    new_product = Product(name=product_data['name'], price=product_data['price'])
    
    # Adding the new product to the session and commit
    db.session.add(new_product)
    db.session.commit()
    
    # Refresh the session to get the latest state of the new product
    db.session.refresh(new_product)
    
    return new_product

def find_all():
    # Retrieving all products
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def search_product(search_term):
    # Searching for products where the name contains the search term
    query = select(Product).where(Product.name.ilike(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products
