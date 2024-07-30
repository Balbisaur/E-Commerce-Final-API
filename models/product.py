from sqlalchemy import Column, Integer, String, Float
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = 'Products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
 