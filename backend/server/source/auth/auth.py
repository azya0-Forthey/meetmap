from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pydantic import BaseModel
from starlette import status

from config import settings

import database.queries.user as users_db
from auth.hashing import verify_pwd
from schemas.user import UserDTO

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
    username: str


async def authenticate_user(username: str, password: str) -> UserDTO | None:
    user = await users_db.get_user(username)

    if not user or not verify_pwd(password, user.password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret.secret_key, algorithm=settings.secret.algorithm)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret.secret_key, algorithms=settings.secret.algorithm)
        user_id: int = payload.get("id")
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(id=user_id, username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = await users_db.get_user(token_data.username)
    if not user:
        raise credentials_exception
    return user

AuthUser = Annotated[UserDTO, Depends(get_current_user)]