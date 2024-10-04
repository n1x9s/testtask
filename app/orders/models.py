from sqlalchemy import Column, Integer, Date, String, ForeignKey
from app.database import Base


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    status = Column(String)


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
