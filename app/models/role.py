from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from sqlalchemy import Enum as SQLEnum
from app.models.enums_role import UserRole
from User_Role import User_Role
from typing import List




class Role(Base):
    """
    Таблица ролей
    """
    __tablename__ = 'roles'
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.USER, server_default=UserRole.USER.value) # Сама роль
    
    user_associations: Mapped[List['User_Role']] = relationship(back_populates="role") # Соединение с таблицей и юзеров и ролей