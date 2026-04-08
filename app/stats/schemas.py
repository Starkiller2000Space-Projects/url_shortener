"""Schemas for `/shorten` endpoint."""

from datetime import datetime

from pydantic import BaseModel


class URLStatsResponse(BaseModel):
    """Statistics response."""

    short_id: str
    original_url: str
    clicks_amount: int
    created_at: datetime
