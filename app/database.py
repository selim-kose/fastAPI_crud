from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from typing import Generator

# SQLAlchemy database URL for MySQL
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/users"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,           # log SQL (disable in prod)
    pool_pre_ping=True   # avoids stale connections
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False,
    bind=engine
)

# Dependency to get DB session 
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base class for models
class Base(DeclarativeBase):
    pass