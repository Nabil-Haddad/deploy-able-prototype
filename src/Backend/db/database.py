from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import DATABASE_URL

# create the engine and the session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This Base class will be inherited by all database models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


