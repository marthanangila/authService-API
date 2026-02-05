from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# the main connection to PostgreSQL
engine = create_engine(settings.DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    # Provides a database session and ensures it's closed after use.
    

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()