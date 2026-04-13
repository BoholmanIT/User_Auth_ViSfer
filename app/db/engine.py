from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings
import asyncio

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asynccopg,
    echo=True,
)


