from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_settings

settings = get_settings()

SessionFactory = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=create_engine(settings.database_dsn)
)

Base = declarative_base()

def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
