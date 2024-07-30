from sqlalchemy import Mapped, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import db, Base
from typing import List

class Role(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    # One-to-Many: Role and Customer
    customers = relationship('Customer', back_populates='role')

class Customer(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True)
    name = Column(db.String(255), nullable=False)
    email = Column(db.String(255), unique=True, nullable=False)
    phone = Column(db.String(20), nullable=False)
    username = Column(db.String(255), unique=True, nullable=False)
    password = Column(db.String(255), nullable=False)
    role_id = Column(db.Integer, ForeignKey('Roles.id'))

    role: Mapped['Role'] = db.relationship()
    # One-to-Many: Customer and Order
    orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")

class Order(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('Customers.id'))

    # Relationship to Customer
    customer = relationship('Customer', back_populates='orders')

