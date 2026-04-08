"""Router for `/` endpoint."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.service import Service as BaseService

from .service import Service

router = APIRouter(prefix="", tags=["Home"])


@router.get("/{short_id}")
async def redirect_to_original(short_id: str, db: Annotated[Session, Depends(get_db)]) -> Response:
    """Redirect to original bounded url.

    Args:
        short_id (str): short url identifier.
        db (Annotated[Session, Depends): database session connection.

    Returns:
        Response: redirection response with original url location.

    Raises:
        HTTPException: when short url is not found.
    """
    url_item = BaseService(db).get_url_by_short_id(short_id)
    if not url_item:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Short URL not found")
    Service(db).increment_clicks(url_item)
    return Response(status_code=HTTPStatus.FOUND, headers={"Location": url_item.original_url})
