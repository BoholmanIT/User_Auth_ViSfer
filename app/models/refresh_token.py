import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.base import Base, Mixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from datetime import datetime
import uuid


class RefreshToken(Base, Mixin):
    """
    Модель для рефреш токена
    """
    __tablename__ = "refreshtokens"
    token_hash: Mapped[str] = mapped_column() # Хэшированный токен
    expires_at: Mapped[datetime] = mapped_column() # До какого годе токен
    revoked: Mapped[bool] = mapped_column(default=False) # Отмененные ли права у пользователя
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id")) #  Внешний ключ с таблицей пользователей
    user = relationship("User", back_populates="refresh_tokens", lazy="select") # Соединение с таблицей пользователей