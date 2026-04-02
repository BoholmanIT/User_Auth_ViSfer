from db.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from user import User

class Profile(Base):
    __tablename__ = 'profiles'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    nickname: Mapped[str] = mapped_column(String(50))
    avatar_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    bio: Mapped[str | None] = mapped_column(String(3072), nullable=True)
    website: Mapped[str | None] = mapped_column(String(512), nullable=True)
    country_code: Mapped[str | None] = mapped_column(String(2))
    city: Mapped[str | None] = mapped_column(String(100))
    last_ip: Mapped[str | None] = mapped_column(String(45))
    user: Mapped["User"] = relationship(back_populates="profile")