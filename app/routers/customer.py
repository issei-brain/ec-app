from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app import schemas
from app import crud

from app.dependency import get_db

router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(
        category: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ):
    items = crud.get_items(db, category=category, skip=skip, limit=limit)
    return items
