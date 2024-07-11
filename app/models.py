from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String)

    orders = relationship("Order", back_populates="item")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer)

    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(DateTime)

    customer = relationship("Item", back_populates="orders")
    item = relationship("Order", back_populates="orders")
