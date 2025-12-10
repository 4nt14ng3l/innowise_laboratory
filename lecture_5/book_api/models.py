from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Base class for all ORM models
Base = declarative_base()

class Book(Base):
    # Define the table name in the database
    __tablename__ = "books"

    # Primary key column, automatically indexed for faster lookups
    id = Column(Integer, primary_key=True, index=True)

    # Title of the book, required (cannot be NULL)
    title = Column(String, nullable=False)

    # Author of the book, required (cannot be NULL)
    author = Column(String, nullable=False)

    # Year of publication, optional (can be NULL)
    year = Column(Integer, nullable=True)
