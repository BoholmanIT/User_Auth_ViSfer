from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID, DateTime, func
import uuid
import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class Base(DeclarativeBase):
    pass

class Mixin():
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # Айди всего
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now()) # Когда создано
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now()) # Когда обновлено