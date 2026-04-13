from session import Factory_AsyncSession
import asyncio



async def get_db():
    try:
        async with Factory_AsyncSession() as session:
            yield session
    
    except Exception as e:
        # Тут должны быть логи
        # Нужно вспоминать привычку все комментить
        # Нужно везде перехватывать ошибки
        # Нужно везде делать логи
        # Место для лога 
        
        # .
        await session.rollback()