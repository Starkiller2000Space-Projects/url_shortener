"""Tests configuration."""

import os
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
os.environ.setdefault("BASE_URL", "http://localhost:8000")
os.environ.setdefault("SHORT_ID_LENGTH", "6")

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db() -> Iterator[Session]:
    """Get database session for testing.

    Yields:
        Iterator[Session]: sqlite database session connection.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def db() -> Iterator[Session]:
    """Create tables in database once per session.

    Yields:
        Iterator[Session]: session with created tables.
    """
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client() -> Iterator[TestClient]:
    """Get client.

    Yields:
        Iterator[TestClient]: get client session.
    """
    with TestClient(app) as c:
        yield c
