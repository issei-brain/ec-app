from sqlalchemy.orm import Session

from . import models, schemas

def get_items(db: Session, category: str | None = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Item)
    if category:
        query = query.filter(models.Item.category == category)
    return query.offset(skip).limit(limit).all()

def create_item(item: schemas.ItemCreate, db: Session):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()

def create_customer(customer: schemas.CustomerCreate, db: Session):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer
