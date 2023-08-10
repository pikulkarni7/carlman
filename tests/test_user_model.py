import pytest
from app.models import User


def test_create_user(client):
    response = client.post(
        "/create_user", json={"email": "test2@example.com", "password": "pass123"}
    )
    assert response.status_code == 201
    assert b"User created successfully" in response.data
