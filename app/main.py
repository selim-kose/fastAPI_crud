from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app import user_service
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MySQL CRUD")


@app.post("/users", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(db, user)


@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    data: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = user_service.update_user(db, user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
