# app/controllers/user_controller.py

from fastapi import APIRouter, HTTPException

from backend.app.dto.models import UserCreateRequest
from backend.app.services.user_service import UserService
from backend.app.models.models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/signup", response_model=dict)
def signup_user(payload: UserCreateRequest):
    try:
        user: User = UserService.create_user(payload.username, payload.password)
        return {"user_id": user.id, "username": user.username}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
