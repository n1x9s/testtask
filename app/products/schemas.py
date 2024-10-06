from decimal import Decimal
from pydantic import BaseModel


class SProduct(BaseModel):
    id: int
    title: str
    description: str
    price: Decimal
    amount: int

    class Config:
        from_attributes = True