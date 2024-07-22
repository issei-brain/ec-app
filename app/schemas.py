from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    category: str
    description: str | None = Field(
        default = None, title="The description of the item", max_length=200
    )

class ItemCreate(ItemBase):
    pass
    
class Item(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CustomerBase(BaseModel):
    name: str = Field(title="The name of the customer", max_length=20)
    age: int | None = Field(
        gt=0, lt=150, description="Age must be greater than 0, less than 150"
        )

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int


class OrderBase(BaseModel):
    item_id: int
    customer_id: int

class Order(OrderBase):
    id: int
    order_date: datetime
    item: Item

    model_config = ConfigDict(from_attributes=True)

class OrderCreate(OrderBase):
    pass
