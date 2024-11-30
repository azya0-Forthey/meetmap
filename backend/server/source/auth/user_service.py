from typing import Annotated

from fastapi import Depends, HTTPException
from jwt import InvalidTokenError
from starlette import status

from auth.token_service import token_service, Token
from auth.hashing import verify_pwd

import database.queries.user as users_db
from schemas.user import UserDTO


class UserService:
    async def login(self, username: str, password: str) -> Token | None:
        user = await users_db.get_user(username)

        if not user or not verify_pwd(password, user.password):
            return None
        if not user:
            return None
        tokens: Token = token_service.generate_tokens(
            payload={
                "id": user.id,
                "username": user.username,
            },
        )
        return tokens

    async def get_current(self, token: str):
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
        # TODO хранить залогированных юзеров в token_service (Redis)
        user = await users_db.get_user(username)
        if not user:
            raise credentials_exception
        return user

    async def logout(self, token: str) -> bool:
        # TODO удалять refresh токен из из бд в token_service (Redis)
        return True

    async def refresh(self, user: UserDTO, token: str) -> Token:
        # TODO проверять валидность refresh токена - через бд в token_service (Redis)
        # TODO обновлять данные юзера из бд (Postgres) - на случай, если в токене устаревшие
        try:
            token_service.decode_refresh_token(token)
            tokens: Token = token_service.generate_tokens(
                payload={
                    "id": user.id,
                    "username": user.username,
                },
            )
            return tokens
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )


user_service = UserService()

AuthUser = Annotated[UserDTO, Depends(user_service.get_current)]
