from sqlalchemy.ext.asyncio import create_async_engine

from config import settings
import asyncio

def async_engine():
    return create_async_engine(url=settings.DATABASE_URL_asynccopg, echo=True,)


