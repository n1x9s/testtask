from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Numeric(10, 2))
    amount = Column(Integer)