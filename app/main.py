from fastapi import FastAPI
from app import user_router

from app import models
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MySQL CRUD")
app.include_router(user_router.router)

