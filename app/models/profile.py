
from app.models.base import Base, Mixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
import uuid

class Profile(Base, Mixin):
    """
    Модель для профилей пользователей
    """
    __tablename__ = 'profiles'
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), unique=True) # Внешний ключ с таблицей пользователей 
    nickname: Mapped[str] = mapped_column(String(50)) # Никнейм пользвателя
    avatar_url: Mapped[str | None] = mapped_column(String(512), nullable=True) # Ссылка на автарку пользователя
    bio: Mapped[str | None] = mapped_column(String(3072), nullable=True) # Описание профиля
    website: Mapped[str | None] = mapped_column(String(512), nullable=True) # Сторонние ссылки профиля на другие ресурсы/соцсети
    country_code: Mapped[str | None] = mapped_column(String(2)) # Код страны
    city: Mapped[str | None] = mapped_column(String(100)) # Город польщователя
    last_ip: Mapped[str | None] = mapped_column(String(45)) # Последний айпи адрес
    user = relationship("User", back_populates="profile") # Соедининение с таблицей пользователей