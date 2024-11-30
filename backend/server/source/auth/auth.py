from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from starlette import status

from auth.token_service import token_service

import database.queries.user as users_db
from auth.hashing import verify_pwd
from schemas.user import UserDTO

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

async def authenticate_user(username: str, password: str) -> UserDTO | None:
    user = await users_db.get_user(username)

    if not user or not verify_pwd(password, user.password):
        return None
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = token_service.decode_access_token(token)
        user_id: int = payload.get("id")
        username: str = payload.get("username")
        if username is None or user_id is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = await users_db.get_user(username)
    if not user:
        raise credentials_exception
    return user

AuthUser = Annotated[UserDTO, Depends(get_current_user)]