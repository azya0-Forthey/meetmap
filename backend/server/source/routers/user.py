from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.util import await_only
from starlette import status

import database.queries.user as user_db
import auth.auth as auth
from config import settings
from schemas.user import UserAddDTO, UserLoginDTO, UserDTO, UserSecureDTO

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/me")
async def get_user_info(user: auth.AuthUser) -> UserSecureDTO:
    return user

@router.post("/login")
async def login_user(form: Annotated[OAuth2PasswordRequestForm, Depends()]) -> auth.Token:
    user = await auth.authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.server.access_token_expire_minutes)
    access_token = auth.create_access_token(
        data={
            "id": user.id,
            "username": user.username,
        },
        expires_delta=access_token_expires
    )
    return auth.Token(access_token=access_token, token_type="bearer")


@router.post("/register")
async def register_user(user: UserAddDTO) -> auth.Token:
    if not await user_db.register_user(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    return await login_user(user)
