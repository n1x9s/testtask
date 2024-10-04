from app.orders.models import Orders
from app.dao.base import BaseDao


class OrderDao(BaseDao):
    model = Orders