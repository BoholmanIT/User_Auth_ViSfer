from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime, func
from datetime import datetime
from role import Role
from user import User
import uuid


class User_Role(Base):
    """
        Модель та самая юзеров ролей
        Нужна для соединение определенной роли и юзера
    """
    __tablename__ = "user_roles"
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True) # Внешний ключ для определения юзера
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), primary_key=True) # Внешний ключ для определенния ролей
    
    granted_at: Mapped[datetime] = mapped_column(server_default=func.now()) # Когда дали определенные права
    granted_by: Mapped[uuid.UUID] = mapped_column(default=None, nullable=True) # Кто дал эти права
    
    
    
    user: Mapped['User'] = relationship(back_populates='role_associations') # Соединение с таблицей юзер
    role: Mapped['Role'] = relationship(back_populates='user_associations')  # Соединение с таблицей ролей
    