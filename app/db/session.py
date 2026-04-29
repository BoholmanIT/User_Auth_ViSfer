from sqlalchemy.ext.asyncio import async_sessionmaker



def Factory_AsyncSession(async_engine)):
    return async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )