from fastapi import FastAPI
from routers import customer, admin

app = FastAPI()

# app.include_router(customer.router, prefix="/customer", tags=["customer"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to ecomerce app"}
