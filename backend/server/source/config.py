from pathlib import Path
from functools import lru_cache
from os import getenv

from pydantic import BaseModel, field_validator, PostgresDsn, ValidationInfo
from pydantic_settings import BaseSettings
from yaml import safe_load
from dotenv import load_dotenv


class Program(BaseSettings):
    DEBUG: bool | None = None

    @field_validator('DEBUG')
    @classmethod
    def validate_debug(cls, value: str | None):    
        if value is not None:
            return value
        
        load_dotenv("../../../.env")
        new_value = getenv("DEBUG")

        if new_value is None:
            raise Exception("TEST")

        return new_value.lower() != "false"


@lru_cache
def get_program_settings():
    return Program()


class Postgres(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    SQLALCHEMY_URL: str | None = None

    @field_validator('POSTGRES_HOST')
    @classmethod
    def validate_db_host(cls, value: str):    
        if get_program_settings().DEBUG:
            return 'localhost'
        return value

    @field_validator('SQLALCHEMY_URL')
    @classmethod
    def validate_sqlalchemy_url(cls, value: str | None, info: ValidationInfo):
        if isinstance(value, str):
            return value

        return str(PostgresDsn.build(
            scheme='postgresql+asyncpg',
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
    program: Program
    postgres: Postgres
    tokens: Tokens


@lru_cache
def get_settings():
    THIS_DIR = Path(__file__).parent

    with Path(f"{THIS_DIR}/../secret.yaml").open("r") as file:
        sub_config = safe_load(file)

    return Settings(
        program=get_program_settings(),
        postgres=Postgres(),
        tokens=Tokens.model_validate(sub_config["tokens"])
    )
