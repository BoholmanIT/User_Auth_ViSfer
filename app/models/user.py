import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.base import Base, Mixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from typing import List

class User(Base, Mixin):
    """
    Таблица юзеров
    """
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False) # Электронная почта
    hashed_password: Mapped[str] = mapped_column(String(100)) # Хэшированные пароли
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False) # Флаг благодаря которому можно отключить юзеров на время не удаляя их из базы данных
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False) # Флаг благадрая которому мы определяем подтвердил ли пользователь почту
    profile = relationship("Profile", back_populates="user", uselist=False)
    role_associations = relationship("User_Role", back_populates="user") # Соединение для таблицы юзеров ролей
    refresh_tokens = relationship("RefreshToken", back_populates="user", lazy="dynamic") # Соедининение для таблицы рефреш токена

    