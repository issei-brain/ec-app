from fastapi import APIRouter, Depends, Query 
from datetime import datetime

from sqlalchemy.orm import Session
from app import schemas
from app import crud

from app.dependency import get_db

router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(
        category: str = Query(default=None, max_length=20),
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
        ):
    items = crud.get_items(db, category=category, skip=skip, limit=limit)
    return items

@router.get("/order/", response_model=list[schemas.Order])
def read_orders(
        customer_id: int,
        order_date_from: datetime = datetime.strptime("2024-07-11 20:00:00", "%Y-%m-%d %H:%M:%S"),
        category: str = "",
        db: Session = Depends(get_db)
        ):
    orders = crud.get_orders_by_customer(db, customer_id = customer_id, order_date_from=order_date_from, category=category)
    return orders

@router.post("/order/", response_model=schemas.Order)
def create_order(
        order: schemas.OrderCreate,
        db: Session = Depends(get_db)
        ):
    order = crud.create_order(db, order=order)
    return order