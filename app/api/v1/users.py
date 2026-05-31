from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_db
from app.services.user_service import get_user_by_id, update_profile
from app.schemas.user import UserOut, ProfileUpdate
from app.api.v1.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/users/me", response_model=UserOut)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/users/me")
async def update_me(update: ProfileUpdate, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    await update_profile(db, current_user.id, update.dict(exclude_unset=True))
    return {"msg": "Profile updated"}