from fastapi import FastAPI
from app.orders.router import router as order_router
from app.products.router import router as product_router


app = FastAPI(
    title='Test API',
    version='1.0',
)
app.include_router(order_router)
app.include_router(product_router)