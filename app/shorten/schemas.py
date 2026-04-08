"""Schemas for `/shorten` endpoint."""

from pydantic import BaseModel, HttpUrl


class URLShortenRequest(BaseModel):
    """Request for url shortening."""

    url: HttpUrl


class URLShortenResponse(BaseModel):
    """URL shortening response schema."""

    short_url: str
    short_id: str
