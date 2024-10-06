from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    status = Column(String)
    items = relationship("OrderItem", backref="order")


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
