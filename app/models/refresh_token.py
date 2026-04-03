from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from datetime import datetime
import uuid
from user import User

class RefreshToken(Base):
    """
    Модель для рефреш токена
    """
    __tablename__ = "refreshtokens"
    token_hash: Mapped[str] = mapped_column() # Хэшированный токен
    expires_at: Mapped[datetime] = mapped_column() # До какого годе токен
    revoked: Mapped[bool] = mapped_column(default=False) # Отмененные ли права у пользователя
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id")) #  Внешний ключ с таблицей пользователей
    user: Mapped["User"] = relationship(back_populates="refresh_tokens", lazy="select") # Соединение с таблицей пользователей