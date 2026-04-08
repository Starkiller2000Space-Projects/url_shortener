"""Database models."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class URLItem(Base):
    """URL item database model."""

    __tablename__ = "urls"

    id: int = Column(Integer, primary_key=True, index=True)
    short_id: str = Column(String, unique=True, index=True, nullable=False)
    original_url: str = Column(String, nullable=False)
    clicks_amount: int = Column(Integer, default=0)
    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())
