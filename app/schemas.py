from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    category: str
    description: str

class ItemCreate(ItemBase):
    pass
    
class Item(ItemBase):
    id: int

    class Config:
        orm_model = True