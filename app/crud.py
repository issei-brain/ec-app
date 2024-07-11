from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas


def get_items(db: Session, category: str | None = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Item)
    if category:
        query = query.filter(models.Item.category == category)
    return query.offset(skip).limit(limit).all()

def create_item(item: schemas.ItemCreate, db: Session):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()

def create_customer(customer: schemas.CustomerCreate, db: Session):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_orders_by_customer(db: Session, customer_id: int,  category: str = "", order_date_from: datetime = datetime.strptime("2024-07-11 20:00:00", "%Y-%m-%d %H:%M:%S")):
    query = db.query(models.Order).filter(models.Order.customer_id == customer_id, models.Order.order_date >= order_date_from)
    if category:
        query = query.join(models.Order.item).filter(models.Item.category == category)
    return query.all()    
