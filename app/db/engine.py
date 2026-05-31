from sqlalchemy.ext.asyncio import create_async_engine
from app.db.config import settings

def async_engine():
    return create_async_engine(url=settings.DATABASE_URL, echo=True)