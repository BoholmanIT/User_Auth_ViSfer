from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.engine import async_engine
from app.db.session import Factory_AsyncSession
from app.api.v1 import auth, users, admin
from app.admin.routes import router as admin_router
from fastapi.responses import HTMLResponse
from app.models.base import Base, Mixin
import app.models

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.engine import async_engine
from app.db.session import Factory_AsyncSession
from app.models.base import Base
import app.models
from app.api.v1 import auth, users, admin
from app.admin.routes import router as admin_router
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = async_engine()
    async with engine.begin() as conn:
        # Создание таблиц
        await conn.run_sync(Base.metadata.create_all)
        
        
    session_factory = Factory_AsyncSession(engine)
    app.state.engine = engine
    app.state.session_factory = session_factory
    yield
    await engine.dispose()
app = FastAPI(title="AuthService", lifespan=lifespan)

# Статика и шаблоны
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/admin/templates")

# API роутеры
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(admin.router, prefix="/api/v1", tags=["admin"])

# Админ панель (HTML)
app.include_router(admin_router, prefix="/admin", tags=["admin-panel"])


