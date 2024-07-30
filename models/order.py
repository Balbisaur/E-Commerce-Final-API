from typing import List
import datetime
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import db, Base
from models.orderProduct import order_product  

class Order(Base):
    __tablename__ = 'Orders'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey('Customers.id'))
    
    # Many-to-One relationship with Customer
    customer = relationship('Customer', back_populates='orders')
    
    # Many-to-Many relationship with Product
    products = relationship('Product', secondary=order_product)
