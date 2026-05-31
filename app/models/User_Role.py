
from app.models.base import Base, Mixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime, func
from datetime import datetime
import uuid
from typing import Optional


class User_Role(Base, Mixin):
    """
        Модель та самая юзеров ролей
        Нужна для соединение определенной роли и юзера
    """
    __tablename__ = "user_roles"
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), primary_key=True) # Внешний ключ для определения юзера
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('roles.id'), primary_key=True) # Внешний ключ для определенния ролей
    
    granted_at: Mapped[datetime] = mapped_column(server_default=func.now()) # Когда дали определенные права
    granted_by: Mapped[uuid.UUID] = mapped_column(default=None, nullable=True) # Кто дал эти права
    expires_at: Mapped[datetime | None] = mapped_column() # До какого момента будет актуальны роль
    revoked: Mapped[bool] = mapped_column(default=False) # Отмененные ли права у пользователя
    
    
    user = relationship("User", back_populates='role_associations') # Соединение с таблицей юзер
    role = relationship("Role", back_populates='user_associations')  # Соединение с таблицей ролей
    