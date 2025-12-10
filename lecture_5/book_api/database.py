from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Database connection URL
# "sqlite:///./books.db" means:
# - Use SQLite as the database engine
# - Store the database file locally in the current directory as "books.db"
DATABASE_URL = "sqlite:///./books.db"

# Create a new SQLAlchemy engine instance
# connect_args={"check_same_thread": False} is required for SQLite
# when using it with multiple threads (e.g., FastAPI requests)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory bound to the engine
# - autoflush=False: changes are not automatically flushed to the database
# - autocommit=False: transactions must be explicitly committed
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Create all tables defined in the models (Base subclasses)
# This ensures that the "books" table is created in the database
Base.metadata.create_all(bind=engine)
