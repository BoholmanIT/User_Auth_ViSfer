from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID, DateTime, func
import uuid
import datetime


class Base(DeclarativeBase):
    __tablename__ = 'bases'
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())