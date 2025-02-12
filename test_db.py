from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

try:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    from sqlalchemy import text
    db.execute(text("SELECT 1"))
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    if db:
        db.close()
