from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the directory of the current file (blog/main.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URL =f"sqlite:///{os.path.join(BASE_DIR, 'blog.db')}"

engine  = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def gets_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

