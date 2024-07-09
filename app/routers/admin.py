from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app import schemas
from app import crud

from app.dependency import get_db

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    items = crud.create_item(item=item, db=db)
    return items

@router.post("/customer/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_name(db, customer.name)
    if db_customer:
        raise HTTPException(status_code=400, detail="Customer already registered")
    return crud.create_customer(db=db, customer=customer)
