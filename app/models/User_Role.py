from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime, func
from datetime import datetime
from role import Role
from user import User
import uuid
class User_Role(Base):
    __tablename__ = "user_roles"
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), primary_key=True)
    
    granted_at: Mapped[datetime] = mapped_column(server_default=func.now())
    granted_by: Mapped[uuid.UUID] = mapped_column(default=None, nullable=True)
    expires
    
    
    user: Mapped['User'] = relationship(back_populates='role_associations')
    role: Mapped['Role'] = relationship(back_populates='user_associations')  
    