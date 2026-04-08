"""Additional functionality for `/shorten` endpoint."""

import random
import string

from sqlalchemy.orm import Session

from app.models import URLItem


class Utils:
    """Additional functionality handler."""

    @staticmethod
    def generate_short_id(length: int) -> str:
        """Generate random string of desired length containing only letters and digits.

        Args:
            length (int): desired string length.

        Returns:
            str:
        """
        chars = string.ascii_letters + string.digits
        return "".join(random.choices(chars, k=length))  # noqa: S311 not security purposes

    @classmethod
    def get_unique_short_id(cls, db: Session, length: int) -> str:
        """Get unique id, that is not present in database.

        Args:
            db (Session): database connection session.
            length (int): desired unique short id length.

        Returns:
            str: unique short id.
        """
        while True:
            short_id = cls.generate_short_id(length)
            if not db.query(URLItem).filter(URLItem.short_id == short_id).first():
                return short_id
