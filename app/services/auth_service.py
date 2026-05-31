from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.models.profile import Profile
from app.models.refresh_token import RefreshToken
from app.models.role import Role
from app.models.User_Role import User_Role
from app.models.enums_role import UserRole
from app.services.password_service import hash_password, verify_password
from datetime import datetime, timedelta
from app.db.config import settings
import uuid
import hashlib

async def register_user(db: AsyncSession, email: str, password: str, nickname: str) -> User:
    # проверка существования
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    if result.scalar_one_or_none():
        raise ValueError("Email already exists")
    hashed = hash_password(password)
    new_user = User(email=email, hashed_password=hashed, is_active=True, is_verified=False)
    db.add(new_user)
    await db.flush()

    profile = Profile(user_id=new_user.id, nickname=nickname)
    db.add(profile)

    # роль USER по умолчанию
    role_stmt = select(Role).where(Role.role == UserRole.USER)
    role_res = await db.execute(role_stmt)
    role = role_res.scalar_one()
    user_role = User_Role(user_id=new_user.id, role_id=role.id)
    db.add(user_role)
    await db.commit()
    return new_user

async def authenticate_user(db: AsyncSession, email: str, password: str) -> User | None:
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

async def create_refresh_token(db: AsyncSession, user_id: uuid.UUID) -> str:
    raw_token = str(uuid.uuid4())
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    expires = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    token = RefreshToken(user_id=user_id, token_hash=token_hash, expires_at=expires, revoked=False)
    db.add(token)
    await db.commit()
    return raw_token

async def get_refresh_token(db: AsyncSession, raw_token: str) -> RefreshToken | None:
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    stmt = select(RefreshToken).where(RefreshToken.token_hash == token_hash, RefreshToken.revoked == False)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def revoke_refresh_token(db: AsyncSession, token: RefreshToken):
    token.revoked = True
    await db.commit()