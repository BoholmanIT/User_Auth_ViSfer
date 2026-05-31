from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.dependencies import get_db
from app.models.user import User
from app.models.role import Role
from app.models.User_Role import User_Role
from app.api.v1.deps import get_current_admin
from app.schemas.user import UserOut
from typing import List

router = APIRouter()

@router.get("/admin/users", response_model=List[UserOut])
async def list_users(db: AsyncSession = Depends(get_db), _=Depends(get_current_admin)):
    stmt = select(User)
    result = await db.execute(stmt)
    users = result.scalars().all()
    return [UserOut(id=u.id, email=u.email, is_active=u.is_active, is_verified=u.is_verified) for u in users]

@router.post("/admin/users/{user_id}/ban")
async def ban_user(user_id: str, db: AsyncSession = Depends(get_db), _=Depends(get_current_admin)):
    from uuid import UUID
    stmt = select(User).where(User.id == UUID(user_id))
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404)
    user.is_active = False
    await db.commit()
    return {"msg": "User banned"}