from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings
DATABASE_URL = "sqlite:///./test.db"
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False},
    echo=True #Veremos si usamos, sirve para el desarrollo
    
)

SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()