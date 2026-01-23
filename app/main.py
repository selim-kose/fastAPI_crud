from fastapi import FastAPI
from app import user_router

app = FastAPI(title="FastAPI MySQL CRUD")
app.include_router(user_router.router)

