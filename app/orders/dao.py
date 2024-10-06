from sqlalchemy import insert, update
from app.orders.models import OrderItem, Orders
from app.dao.base import BaseDao

from app.database import async_session


class OrderDao(BaseDao):
    model = Orders

    @staticmethod
    async def add_item(order_id, product_id, quantity):
        async with async_session() as session:
            query = insert(OrderItem).values(order_id=order_id, product_id=product_id, quantity=quantity)
            await session.execute(query)
            await session.commit()

    
    @staticmethod
    async def update_status(order_id, status):
        async with async_session() as session:
            query = (
                update(Orders)
                .where(Orders.id == order_id)
                .values(
                    status=status
                )
            )
            await session.execute(query)
            await session.commit()