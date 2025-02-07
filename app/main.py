from fastapi import FastAPI, HTTPException

from app import models
from app.database import engine

from app.routers import customer, admin

app = FastAPI()

app.include_router(customer.router, prefix="/customer", tags=["customer"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to ecomerce app"}


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)