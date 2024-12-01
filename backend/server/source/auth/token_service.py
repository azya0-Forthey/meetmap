from datetime import timedelta, datetime, timezone

import jwt
from pydantic import BaseModel

from config import settings


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenService:
    _access_secret_key: str
    _refresh_secret_key: str
    _encode_algorithm: str
    _access_token_expire_minutes: int
    _refresh_token_expire_minutes: int

    def __init__(self):
        self._access_secret_key = settings.tokens.access_secret_key
        self._refresh_secret_key = settings.tokens.refresh_secret_key
        self._encode_algorithm = settings.tokens.algorithm
        self._access_token_expire_minutes = settings.tokens.access_token_expire_minutes
        self._refresh_token_expire_minutes = settings.tokens.refresh_token_expire_minutes

    def _parse_payload(self, payload: dict, expire_time: timedelta) -> dict:
        to_encode = payload.copy()
        exp_time = datetime.now(timezone.utc) + expire_time
        to_encode.update({"exp": exp_time})
        return to_encode

    def _create_access_token(self, payload: dict) -> str:
        return jwt.encode(self._parse_payload(payload, timedelta(minutes=self._access_token_expire_minutes)),
                          self._access_secret_key,
                          algorithm=self._encode_algorithm)

    def _create_refresh_token(self, payload: dict) -> str:
        return jwt.encode(self._parse_payload(payload, timedelta(minutes=self._refresh_token_expire_minutes)),
                          self._refresh_secret_key,
                          algorithm=self._encode_algorithm)

    def generate_tokens(self, payload: dict) -> Token:
        return Token(
            access_token=self._create_access_token(payload),
            refresh_token=self._create_refresh_token(payload),
            token_type='Bearer'
        )

    def decode_access_token(self, token: str) -> dict:
        return jwt.decode(token, self._access_secret_key, algorithms=self._encode_algorithm)

    def decode_refresh_token(self, token: str) -> dict:
        return jwt.decode(token, self._refresh_secret_key, algorithms=self._encode_algorithm)


token_service = TokenService()
