from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.util import await_only
from starlette import status

import database.queries.user as user_db
import auth.auth as auth
from auth.token_service import token_service, Token
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
async def login_user(form: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response) -> Token:
    user = await auth.authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    tokens: Token = token_service.generate_tokens(
        payload={
            "id": user.id,
            "username": user.username,
        },
    )
    response.set_cookie("refresh_token", tokens.refresh_token,
                        max_age=settings.tokens.access_token_expire_minutes * 60 * 1000, httponly=True)
    return tokens


@router.post("/register")
async def register_user(user: UserAddDTO) -> int:
    user_id = await user_db.register_user(user)
    if not id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    return user_id
