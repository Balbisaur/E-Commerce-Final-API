from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, ForeignKey
from database import db, Base
from typing import List
from models.order import Order



class Customer(Base):
    __tablename__ = 'Customers'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(db.String(255), nullable=False)
    email = mapped_column(db.String(255), unique=True, nullable=False)
    phone = mapped_column(db.String(20), nullable=False)
    username = mapped_column(db.String(255), unique=True, nullable=False)
    password = mapped_column(db.String(255), nullable=False)
    role_id = mapped_column(db.Integer, ForeignKey('Roles.id'))

    role: mapped_column['Role'] = db.relationship()
    # One-to-Many: Customer and Order
    orders: mapped_column[List["Order"]] = db.relationship(back_populates="customer")
