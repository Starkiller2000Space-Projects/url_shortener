"""Tests for `/shorten` endpoint."""

import string

from pytest_mock import MockerFixture

from app.shorten.service import Service
from app.shorten.utils import Utils

# utils


def test_generate_short_id_length() -> None:
    """Test generate short id."""
    DESIRED_LENGTH = 6
    short_id = Utils.generate_short_id(DESIRED_LENGTH)
    assert len(short_id) == DESIRED_LENGTH
    assert all(c in string.ascii_letters + string.digits for c in short_id)


def test_get_unique_short_id_returns_unique(mocker: MockerFixture) -> None:
    """Test whether only unique ids are received.

    Args:
        mocker (MockerFixture): mocker fixture from pytest.
    """
    EXISTING_VALUE, NONEXISTING_VALUE = "abc123", "def456"
    mock_db = mocker.Mock()  # database mock
    # first value does exist, second does not
    mock_db.query.return_value.filter.return_value.first.side_effect = [True, False]
    mocker.patch("app.shorten.utils.Utils.generate_short_id", side_effect=[EXISTING_VALUE, NONEXISTING_VALUE])
    result = Utils.get_unique_short_id(mock_db, 6)
    assert result == NONEXISTING_VALUE  # first value must be skipped
    assert mock_db.query.call_count == 2


# service


def test_create_short_url(mocker: MockerFixture) -> None:
    """Test short url creation.

    Args:
        mocker (MockerFixture): mocker fixture from pytest.
    """
    EXPECTED_ID = "test123"
    EXPECTED_URL = "https://example.com"
    mock_db = mocker.Mock()
    mock_get_unique = mocker.patch("app.shorten.service.Utils.get_unique_short_id", return_value=EXPECTED_ID)
    mock_db.add = mocker.Mock()
    mock_db.commit = mocker.Mock()
    mock_db.refresh = mocker.Mock()

    result = Service(mock_db).create_short_url(EXPECTED_URL)

    mock_get_unique.assert_called_once_with(mock_db, 6)
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()
    assert result.short_id == EXPECTED_ID
    assert result.original_url == EXPECTED_URL
