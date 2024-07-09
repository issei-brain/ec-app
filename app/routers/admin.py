from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app import schemas
from app import crud

from app.dependency import get_db

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    items = crud.create_item(item=item, db=db)
    return items