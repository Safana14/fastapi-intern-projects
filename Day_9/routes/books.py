#Create APIRouter
from fastapi import APIRouter, HTTPException
from models import Book

router = APIRouter()

books = {}

#Create GET All Books
@router.get("/books")
def get_books():
    return books

#Create GET Single Book
@router.get("/books/{book_id}")
def get_book(book_id: int):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[book_id]

#Create POST Endpoint
@router.post("/books")
def create_book(book_id: int, book: Book):

    books[book_id] = book

    return {
        "message": "Book created",
        "book": book
    }

#Create PUT Endpoint
@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    books[book_id] = book

    return {
        "message": "Book updated",
        "book": book
    }

#Create DELETE Endpoint
@router.delete("/books/{book_id}")
def delete_book(book_id: int):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    deleted = books.pop(book_id)

    return {
        "message": "Book deleted",
        "book": deleted
    }