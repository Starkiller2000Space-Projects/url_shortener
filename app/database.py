"""Database handling."""

from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, Session, declarative_base, sessionmaker

from app.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db() -> Iterator[Session]:  # pragma: no cover
    """Get database session.

    Yields:
        Iterator[sessionmaker]: database session and then closes it.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
