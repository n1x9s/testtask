from fastapi import APIRouter
from app.orders.dao import OrderDao
from app.orders.schemas import SOrderItem, SOrders, Status

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("")  # Создание заказа (POST /orders)
async def create_order(order: SOrders):
    return await OrderDao.add(date=order.date, status=order.status)

@router.post("/item")  # Создание элемента заказа (POST /orders/item)
async def create_order_item(order_item: SOrderItem):
    return await OrderDao.add_item(order_id=order_item.order_id, product_id=order_item.product_id, quantity=order_item.quantity)


@router.get("")  # Получение списка заказов (GET /orders)
async def get_all_orders():
    return await OrderDao.get_all()


@router.get("/{order_id}")  # Получение информации о заказе по id (GET /orders/{id})
async def get_order_by_id(order_id: int):
    return await OrderDao.get(order_id)


@router.patch("/{order_id}/status")  # Обновление статуса заказа (PATCH /orders/{id}/status)
async def update_order_status(order_id: int, status: Status):
    return await OrderDao.update_status(order_id=order_id, status=status)
