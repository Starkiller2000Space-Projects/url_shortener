"""Integration tests."""

from http import HTTPStatus

from fastapi.testclient import TestClient


def test_create_short_url(client: TestClient) -> None:
    """Test short link creation.

    Args:
        client (TestClient): client fixture from conftest.
    """
    response = client.post("/shorten", json={"url": "https://example.com/short/url/creation/test"})
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert "short_url" in data
    assert "short_id" in data
    assert str(data["short_url"]).endswith(data["short_id"])


def test_multiple_redirects_increment_clicks(client: TestClient) -> None:
    """Test multiple redirects increase clicks amount 1 to 1.

    Args:
        client (TestClient): client fixture from conftest.
    """
    REDIRECTS_AMOUNT = 3
    create_resp = client.post("/shorten", json={"url": "https://example.com/nultiple/redirection/test"})
    short_id: str = create_resp.json()["short_id"]
    original_amount = client.get(f"/stats/{short_id}").json()["clicks_amount"]

    for _ in range(REDIRECTS_AMOUNT):
        resp = client.get(f"/{short_id}", follow_redirects=False)
        assert resp.status_code == HTTPStatus.FOUND

    stats = client.get(f"/stats/{short_id}").json()
    assert stats["clicks_amount"] == original_amount + REDIRECTS_AMOUNT


def test_nonexistent_short_id_returns_404(client: TestClient) -> None:
    """Test whether nonexistent short id returns status code Not Found.

    Args:
        client (TestClient): client fixture from conftest.
    """
    resp = client.get("/nonexistent")
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.json()["detail"] == "Short URL not found"


def test_stats_for_nonexistent_returns_404(client: TestClient) -> None:
    """Test whether nonexistent short id passed to `/stats` endpoint returns status code Not Found.

    Args:
        client (TestClient): client fixture from conftest.
    """
    resp = client.get("/stats/nonexistent")
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.json()["detail"] == "Short URL not found"
