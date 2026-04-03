from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID, DateTime, func
import uuid
import datetime
from models.profile import Profile
from models.refresh_token import RefreshToken
from models.role import Role
from models.User_Role import User_Role
from models.user import User


class Base(DeclarativeBase):
    '''
    Базавая модель
    '''
    
    __tablename__ = 'bases'
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # Айди всего
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now()) # Когда создано
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now()) # Когда обновлено