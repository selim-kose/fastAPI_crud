from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from typing import Generator
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_USERNAME=os.getenv("DB_USERNAME", "user")
DB_PASSWORD=os.getenv("DB_PASSWORD", "password")
DB_HOST=os.getenv("DB_HOST", "localhost")
DB_PORT=os.getenv("DB_PORT", "3306")
DB_NAME=os.getenv("DB_NAME", "users")

# SQLAlchemy database URL for MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#DATABASE_URL = "mysql+pymysql://user:password@mysql:3306/users"

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

#FastAPI Dependency injection mechanism, to get a DB session 
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base class for models
class Base(DeclarativeBase):
    pass