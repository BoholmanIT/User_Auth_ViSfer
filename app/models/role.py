
from app.models.base import Base, Mixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from sqlalchemy import Enum as SQLEnum
from app.models.enums_role import UserRole
from typing import List




class Role(Base, Mixin):
    """
    Таблица ролей
    """
    __tablename__ = 'roles'
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.USER, server_default=UserRole.USER.value) # Сама роль
    
    user_associations = relationship("User_Role", back_populates="role") # Соединение с таблицей и юзеров и ролей