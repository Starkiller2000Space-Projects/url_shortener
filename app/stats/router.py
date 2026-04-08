"""Router for stats/ endpoint."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.service import Service as BaseService

from .schemas import URLStatsResponse

router = APIRouter(prefix="/stats", tags=["Stats"])


@router.get("/{short_id}", response_model=URLStatsResponse)
async def get_stats(short_id: str, db: Annotated[Session, Depends(get_db)]) -> URLStatsResponse:
    """Get statiscics corresponding to unique short identifier.

    Args:
        short_id (str): unique short identifier.
        db (Annotated[Session, Depends): database session connection.

    Returns:
        URLStatsResponse: response containing statistics information.

    Raises:
        HTTPException: when original url not found by given short identifier.
    """
    url_item = BaseService(db).get_url_by_short_id(short_id)
    if not url_item:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Short URL not found")
    return URLStatsResponse(
        short_id=url_item.short_id,
        original_url=url_item.original_url,
        clicks_amount=url_item.clicks_amount,
        created_at=url_item.created_at,
    )
