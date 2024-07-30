from database import db, Base

# Association table for the many-to-many relationship between Orders and Products
order_product = db.Table(
    'order_product',  # Table name, typically snake_case
    Base.metadata,
    db.Column('order_id', db.Integer, db.ForeignKey('Orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('Products.id'), primary_key=True)
)
