from pydantic import BaseModel
from datetime import date
from enum import Enum

class Status(str, Enum):
    in_progress = 'в процессе'
    sent = 'отправлен'
    delivered = 'доставлен'


class SOrders(BaseModel):
    date: date
    status: Status

    class Config:
        from_attributes = True


class SOrderItem(BaseModel):
    order_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True