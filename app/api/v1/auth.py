from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...db.dependencies import get_db
from ...schemas.token import LoginRequest, Token, RefreshRequest
from ...schemas.user import UserCreate, UserOut
from ...services.auth_service import register_user, authenticate_user, create_refresh_token, get_refresh_token, revoke_refresh_token
from ...services.token_service import create_access_token, decode_token
from ...models.user import User
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        user = await register_user(db, user_data.email, user_data.password, user_data.display_name)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
async def login(creds: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, creds.email, creds.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id), "role": user.role_associations[0].role.role.value})
    refresh_token = await create_refresh_token(db, user.id)
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=Token)
async def refresh(req: RefreshRequest, db: AsyncSession = Depends(get_db)):
    token_obj = await get_refresh_token(db, req.refresh_token)
    if not token_obj or token_obj.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
    user = token_obj.user
    new_access = create_access_token({"sub": str(user.id)})
    new_refresh = await create_refresh_token(db, user.id)
    await revoke_refresh_token(db, token_obj)
    return Token(access_token=new_access, refresh_token=new_refresh)

@router.post("/logout")
async def logout(req: RefreshRequest, db: AsyncSession = Depends(get_db)):
    token_obj = await get_refresh_token(db, req.refresh_token)
    if token_obj:
        await revoke_refresh_token(db, token_obj)
    return {"msg": "Logged out"}