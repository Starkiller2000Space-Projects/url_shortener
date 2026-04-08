"""Tests for `/` endpoint."""

from pytest_mock import MockerFixture

from app.core.service import Service
from app.models import URLItem


def test_increment_clicks(mocker: MockerFixture) -> None:
    """Test clicks amount gets incremented.

    Args:
        mocker (MockerFixture): mocker fixture from pytest.
    """
    mock_db = mocker.Mock()
    mock_db.commit = mocker.Mock()
    ORIGINAL_CLICKS_AMOUNT = 5
    url_item = URLItem(short_id="abc", original_url="https://test.com", clicks_amount=ORIGINAL_CLICKS_AMOUNT)
    Service(mock_db).increment_clicks(url_item)
    assert url_item.clicks_amount == ORIGINAL_CLICKS_AMOUNT + 1
    mock_db.commit.assert_called_once()
