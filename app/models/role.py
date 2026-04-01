from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from sqlalchemy import Enum as SQLEnum
from app.models.enums_role import UserRole





class Role(Base):
    
    __tablename__ = 'roles'
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.USER, server_default=UserRole.USER.value)
    
    user_associations: Mapped[List['User_Role']] = relationship(back_populates="role")