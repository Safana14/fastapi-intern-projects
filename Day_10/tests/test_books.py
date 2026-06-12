from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books?book_id=1",
        json={
            "title": "Python Basics",
            "author": "John",
            "price": 500.0
        }
    )

    assert response.status_code == 200


def test_get_books():
    response = client.get("/books")

    assert response.status_code == 200


def test_get_book():
    response = client.get("/books/1")

    assert response.status_code == 200


def test_update_book():
    response = client.put(
        "/books/1",
        json={
            "title": "Advanced Python",
            "author": "John",
            "price": 700.0
        }
    )

    assert response.status_code == 200


def test_delete_book():
    response = client.delete("/books/1")

    assert response.status_code == 200