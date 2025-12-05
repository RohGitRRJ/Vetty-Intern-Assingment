from fastapi.testclient import TestClient

from app.main import app
from app.config import get_settings

client = TestClient(app)


def test_login_success():
    settings = get_settings()
    response = client.post(
        "/auth/login",
        data={
            "username": settings.demo_username,
            "password": settings.demo_password,
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert "access_token" in payload
    assert payload["token_type"] == "bearer"


def test_login_failure():
    response = client.post(
        "/auth/login",
        data={"username": "not-a-user", "password": "bad-pass"},
    )
    assert response.status_code == 401
