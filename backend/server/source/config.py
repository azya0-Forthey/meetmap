from pathlib import Path
from functools import lru_cache

from pydantic import BaseModel, field_validator, PostgresDsn, ValidationInfo
from pydantic_settings import BaseSettings
from yaml import safe_load

class Postgres(BaseSettings):
    DEBUG: bool

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    SQLALCHEMY_URL: str | None = None

    @field_validator('POSTGRES_HOST')
    @classmethod
    def validate_db_host(cls, value: str, info: ValidationInfo):
        if info.data["DEBUG"]:
            return 'localhost'
        return value

    @field_validator('SQLALCHEMY_URL')
    @classmethod
    def validate_sqlalchemy_url(cls, value: str | None, info: ValidationInfo):
        if isinstance(value, str):
            return value

        # TODO change psycopg to asyncpg
        return str(PostgresDsn.build(
            scheme='postgresql+psycopg',
            username=info.data["POSTGRES_USER"],
            password=info.data["POSTGRES_PASSWORD"],
            host=info.data["POSTGRES_HOST"],
            port=info.data["POSTGRES_PORT"],
            path=info.data["POSTGRES_DB"],
        ))


class Tokens(BaseModel):
    access_secret_key: str
    refresh_secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int


class Settings(BaseModel):
    postgres: Postgres
    tokens: Tokens

    @property
    def get_psycopg_url(self):
        if self.postgres.SQLALCHEMY_URL is None:
            raise Exception("miss SQLALCHEMY_URL")
        return self.postgres.SQLALCHEMY_URL


THIS_DIR = Path(__file__).parent


@lru_cache
def get_settings():
    with Path(f"{THIS_DIR}/../secret.yaml").open("r") as file:
        sub_config = safe_load(file)

    return Settings(postgres=Postgres(), tokens=Tokens.model_validate(sub_config["tokens"]))


# TODO change all settings imports to get_settings()
settings = get_settings()