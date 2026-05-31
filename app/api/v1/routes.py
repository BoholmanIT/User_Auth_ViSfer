from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.api.v1.deps import get_current_user
from app.models.user import User

router = APIRouter()
templates = Jinja2Templates(directory="app/admin/templates")

@router.get("/")
async def admin_dashboard(request: Request, current_user: User = Depends(get_current_user)):
    # проверка роли admin
    roles = [ur.role.role for ur in current_user.role_associations]
    if "ADMIN" not in roles:
        return templates.TemplateResponse("error.html", {"request": request, "msg": "Access denied"})
    return templates.TemplateResponse("index.html", {"request": request, "user": current_user})