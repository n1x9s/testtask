from app.products.models import Products
from app.dao.base import BaseDao

from app.database import async_session
from sqlalchemy import delete, update


class ProductsDao(BaseDao):
    model = Products

    @staticmethod
    async def delete(product_id):
        async with async_session() as session:
            query = delete(Products).where(Products.id == product_id)
            await session.execute(query)
            await session.commit()

    
    @staticmethod
    async def update(product_id, title=None, description=None, price=None, amount=None):
        async with async_session() as session:
            query = (
                update(Products)
                .where(Products.id == product_id)
                .values(
                    title=title,
                    description=description,
                    price=price,
                    amount=amount
                )
            )
            await session.execute(query)
            await session.commit()
