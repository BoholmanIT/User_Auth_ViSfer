from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from User_Role import User_Role
from typing import List
from profile import Profile
from refresh_token import RefreshToken

class User(Base):
    """
    Таблица юзеров
    """
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False) # Электронная почта
    hashed_password: Mapped[str] = mapped_column(String(100)) # Хэшированные пароли
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False) # Флаг благодаря которому можно отключить юзеров на время не удаляя их из базы данных
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False) # Флаг благадрая которому мы определяем подтвердил ли пользователь почту
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)
    role_associations: Mapped[List['User_Role']] = relationship(back_populates="user") # Соединение для таблицы юзеров ролей
    refresh_tokens: Mapped["RefreshToken"] = relationship(back_populates="user", lazy="dynamic")

    