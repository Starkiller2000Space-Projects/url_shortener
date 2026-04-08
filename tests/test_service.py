"""Tests for common service functionality."""

from pytest_mock import MockerFixture

from app.models import URLItem
from app.service import Service

# service


def test_get_url_by_short_id_found(mocker: MockerFixture) -> None:
    """Test get url by short id.

    Args:
        mocker (MockerFixture): mocker fixture from pytest.
    """
    mock_db = mocker.Mock()
    SHORT_ID = "abc"
    expected_item = URLItem(short_id=SHORT_ID, original_url="https://test.com")
    mock_db.query.return_value.filter.return_value.first.return_value = expected_item

    result = Service(mock_db).get_url_by_short_id(SHORT_ID)
    assert result == expected_item


def test_get_url_by_short_id_not_found(mocker: MockerFixture) -> None:
    """Test get nonexisting url by short id.

    Args:
        mocker (MockerFixture): mocker fixture from pytest.
    """
    mock_db = mocker.Mock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    result = Service(mock_db).get_url_by_short_id("missing")
    assert result is None
