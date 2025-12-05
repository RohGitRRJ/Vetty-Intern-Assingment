from fastapi.testclient import TestClient

from app.main import app
from app.config import get_settings

client = TestClient(app)


def _get_token() -> str:
    settings = get_settings()
    response = client.post(
        "/auth/login",
        data={
            "username": settings.demo_username,
            "password": settings.demo_password,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def test_list_coins_requires_auth():
    response = client.get("/coins?page_num=1&per_page=3")
    assert response.status_code == 401


def test_list_coins_authorised():
    token = _get_token()
    response = client.get(
        "/coins?page_num=1&per_page=3",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["page_num"] == 1
    assert body["per_page"] == 3
    assert len(body["items"]) <= 3
