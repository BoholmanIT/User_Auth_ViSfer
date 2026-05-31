from fastapi import Request

async def get_db(request: Request):
    async with request.app.state.session_factory() as session:
        yield session