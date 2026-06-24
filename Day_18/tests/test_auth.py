from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_endpoint():
    response = client.post(
        "/auth/register",
        json={
            "username": "pytestuser",
            "email": "pytest@example.com",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 400]