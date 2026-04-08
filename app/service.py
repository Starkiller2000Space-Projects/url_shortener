"""Service handling for all endpoints."""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.models import URLItem


@dataclass
class Service:
    """Service handler for `/shorten` endpoint."""

    db: Session

    def get_url_by_short_id(self, short_id: str) -> URLItem | None:
        """Get url by its unique short identifier.

        Args:
            short_id (str): short unique id.

        Returns:
            URLItem | None: found url item data or None.
        """
        return self.db.query(URLItem).filter(URLItem.short_id == short_id).first()
