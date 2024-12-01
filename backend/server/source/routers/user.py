import logging
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.params import Cookie
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

import database.queries.user as user_db
from auth.token_service import token_service, Token
from auth.user_service import user_service, AuthUser
from config import settings
from schemas.user import UserAddDTO, UserLoginDTO, UserDTO, UserSecureDTO

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me")
async def get_user_info(user: AuthUser) -> UserSecureDTO:
    return user


@router.post("/login")
async def login_user(user: UserLoginDTO, response: Response) -> Token:
    tokens = await user_service.login(user.username, user.password)
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"Authorization": "Bearer"},
        )
    response.set_cookie("refresh_token", tokens.refresh_token,
                        max_age=settings.tokens.access_token_expire_minutes * 60 * 1000, httponly=True)
    return tokens


@router.post("/register")
async def register_user(user: UserAddDTO) -> int:
    user_id = await user_db.register_user(user)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    return user_id

@router.post("/logout")
async def logout_user(refresh_token: Annotated[str, Cookie()], response: Response):
    await user_service.logout(refresh_token)
    response.delete_cookie("refresh_token")

@router.get("/refresh")
async def refresh_user(refresh_token: Annotated[str, Cookie()], response: Response) -> Token:
    tokens = await user_service.refresh(refresh_token)
    response.set_cookie("refresh_token", tokens.refresh_token,
                        max_age=settings.tokens.access_token_expire_minutes * 60 * 1000, httponly=True)
    return tokens