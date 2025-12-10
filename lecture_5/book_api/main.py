from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Book
from .schemas import BookCreate, BookRead

# Initialize FastAPI application
app = FastAPI()


# Dependency for database session management
# Each request gets its own session, which is closed after use
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📌 Add a new book
@app.post("/books/", response_model=BookRead)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to dictionary and create a new Book instance
    new_book = Book(**book.model_dump())
    db.add(new_book)          # Add to session
    db.commit()               # Commit transaction
    db.refresh(new_book)      # Refresh instance with DB data (e.g., auto-generated ID)
    return new_book


# 📌 Get list of books with pagination
@app.get(
    "/books/",
    response_model=list[BookRead],
    summary="Get list of books",
    description="Returns a list of books with pagination support"
)
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of books.
    - **skip**: number of records to skip
    - **limit**: maximum number of records to return
    """
    return db.query(Book).offset(skip).limit(limit).all()


# 📌 Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        # Raise 404 error if book not found
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)   # Remove from session
    db.commit()       # Commit transaction
    return {"message": "Book deleted"}


# 📌 Update a book by ID
@app.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, updated: BookCreate, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        # Raise 404 error if book not found
        raise HTTPException(status_code=404, detail="Book not found")
    # Update fields dynamically from provided data
    for key, value in updated.model_dump().items():
        setattr(book, key, value)
    db.commit()       # Commit changes
    db.refresh(book)  # Refresh instance with updated data
    return book


# 📌 Search books by title, author, or year
@app.get("/books/search/", response_model=list[BookRead])
def search_books(title: str = "", author: str = "", year: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year is not None:
        query = query.filter(Book.year == year)
    return query.all()
