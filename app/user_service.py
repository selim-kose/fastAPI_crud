from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, data: UserUpdate):
    user = get_user(db, user_id)
    if not user:
        return None

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
