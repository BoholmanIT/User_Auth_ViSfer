from sqlalchemy.ext.asyncio import async_sessionmaker

from .engine import async_engine

def Factory_AsyncSession(async_engine):
    return async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )