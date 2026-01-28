import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient

# 1. Vi använder SQLite i minnet. StaticPool krävs för att hålla 
# anslutningen öppen mellan olika funktioner under ett och samma test.
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
    """Skapar en ren databas för varje enskilt test."""
    Base.metadata.create_all(bind=engine) # Skapa tabeller
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine) # Radera allt efter testet

@pytest.fixture
def client(db_session):
    """Skapar en TestClient som använder vår test-databas."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    # Vi byter ut den riktiga get_db mot vår test-variant
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]