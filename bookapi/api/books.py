from fastapi import APIRouter

from models.books import books


router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


# Get all books
@router.get("/")
async def get_books():
    return books


# Get a single book by isbn
@router.get("/{isbn}")
async def get_book(isbn: str):
    for book in books:
        if book["isbn"] == isbn:
            return book
    return {"detail": "Book not found"}


# Add a new book
@router.post("/")
async def add_book(book: dict):
    books.append(book)
    return {"detail": "Book added"}


# Update a book
@router.put("/{isbn}")
async def update_book(isbn: str, book: dict):
    for index, b in enumerate(books):
        if b["isbn"] == isbn:
            book["isbn"] = isbn
            books[index] = book
            return {"detail": "Book updated"}
    return {"detail": "Book not found"}


# Delete a book
@router.delete("/{isbn}")
async def delete_book(isbn: str):
    for index, book in enumerate(books):
        if book["isbn"] == isbn:
            del books[index]
            return {"detail": "Book deleted"}
    return {"detail": "Book not found"}
