from pydantic import BaseModel, EmailStr
from datetime import datetime

# Pydantic schemas for User
class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

# Schema for creating a user
class UserCreate(UserBase):
    pass

# Schema for updating a user
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None

# Schema for responding with user data
class UserResponse(UserBase):
    id: int
    date_created: datetime

    # ORM mode to work with SQLAlchemy models
    class Config:
        from_attributes = True  # SQLAlchemy compatibility
