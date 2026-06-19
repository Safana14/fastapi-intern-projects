import asyncio
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def override_get_db():
    async with TestSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    async def init_models():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())
    yield


client = TestClient(app)

TEST_USER = {"username": "testuser", "email": "testuser@example.com", "password": "TestPass123"}


@pytest.fixture(scope="module")
def auth_token():
    client.post("/auth/register", json=TEST_USER)
    response = client.post(
        "/auth/login",
        json={"email": TEST_USER["email"], "password": TEST_USER["password"]},
    )
    return response.json()["access_token"]


def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


def test_register_user():
    response = client.post("/auth/register", json={
        "username": "newuser1", "email": "newuser1@example.com", "password": "Pass123!"
    })
    assert response.status_code in (200, 201, 400)


def test_login_user(auth_token):
    assert isinstance(auth_token, str) and len(auth_token) > 0


def test_login_invalid_credentials():
    response = client.post("/auth/login", json={"email": "nouser@example.com", "password": "wrong"})
    assert response.status_code == 401


def test_create_task(auth_token):
    response = client.post(
        "/tasks",
        json={"title": "Finish report", "description": "I am so happy with the progress"},
        headers=auth_headers(auth_token),
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_tasks(auth_token):
    response = client.get("/tasks", headers=auth_headers(auth_token))
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task(auth_token):
    create = client.post(
        "/tasks",
        json={"title": "Old title", "description": "desc"},
        headers=auth_headers(auth_token),
    )
    task_id = create.json()["id"]
    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "New title", "description": "updated desc", "completed": False},
        headers=auth_headers(auth_token),
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New title"


def test_delete_task(auth_token):
    create = client.post(
        "/tasks",
        json={"title": "Temp task", "description": "to delete"},
        headers=auth_headers(auth_token),
    )
    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}", headers=auth_headers(auth_token))
    assert response.status_code == 200


def test_sentiment_endpoint(auth_token):
    create = client.post(
        "/tasks",
        json={"title": "Great job team", "description": "I am thrilled with the results"},
        headers=auth_headers(auth_token),
    )
    task_id = create.json()["id"]
    response = client.post(f"/tasks/{task_id}/sentiment", headers=auth_headers(auth_token))
    assert response.status_code == 200
    data = response.json()
    assert data["label"] in ("POSITIVE", "NEGATIVE")
    assert 0 <= data["score"] <= 1