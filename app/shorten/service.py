"""Service handling for `/shorten` endpoint."""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.config import settings
from app.models import URLItem

from .utils import Utils


@dataclass
class Service:
    """Service handler for `/shorten` endpoint."""

    db: Session

    def create_short_url(self, original_url: str) -> URLItem:
        """Create short url for given url and remember this bound.

        Args:
            original_url (str): given url to create short url for.

        Returns:
            URLItem: database url item data.
        """
        short_id = Utils.get_unique_short_id(self.db, settings.SHORT_ID_LENGTH)
        db_item = URLItem(short_id=short_id, original_url=original_url)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
