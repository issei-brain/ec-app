from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def read_items():
    return {"message": "this is read_items"}