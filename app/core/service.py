"""Service handling for `/shorten` endpoint."""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.models import URLItem


@dataclass
class Service:
    """Service handler for `/shorten` endpoint."""

    db: Session

    def increment_clicks(self, url_item: URLItem) -> None:
        """Increments clicks by database item unique id.

        Args:
            url_item (URLItem): database item data.
        """
        url_item.clicks_amount += 1
        self.db.commit()
