from fastapi import APIRouter

import database.queries.user as user_db
from schemas.placemark import PlaceMarkDTO
from schemas.user import UserAddDTO

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/register", response_model=int)
async def register_user(user: UserAddDTO):
    return await user_db.register_user(user)