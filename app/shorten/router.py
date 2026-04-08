"""Router for `/shorten` endpoint."""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db

from .schemas import URLShortenRequest, URLShortenResponse
from .service import Service

router = APIRouter(prefix="/shorten", tags=["Shorten"])


@router.post("")
async def shorten_url(request: URLShortenRequest, db: Annotated[Session, Depends(get_db)]) -> URLShortenResponse:
    """Shorted given url and return short version.

    Args:
        request (URLShortenRequest): sent request.
        db (Annotated[Session, Depends): database session connection.

    Returns:
        URLShortenResponse: response containing short url and short id.
    """
    url_item = Service(db).create_short_url(str(request.url))
    short_url = f"{settings.BASE_URL}/{url_item.short_id}"
    return URLShortenResponse(short_url=short_url, short_id=url_item.short_id)
