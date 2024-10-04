from sqlalchemy import Column, Integer, Date, String

from app.database import Base


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    amount = Column(Integer)