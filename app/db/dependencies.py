from session import Factory_AsyncSession
import asyncio
from fastapi import Request


async def get_db(request: Request):
    try:
        async with request.app.state.session_factory() as session:
            yield session
    
    except Exception as e:
        # Тут должны быть логи
        # Нужно вспоминать привычку все комментить
        # Нужно везде перехватывать ошибки
        # Нужно везде делать логи
        # Место для лога 
        print(e)