from pydantic import BaseModel

class Item(BaseModel):
    name: str
    category: str
    description: str

