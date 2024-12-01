from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from yaml import safe_load


class Postgres(BaseModel):
    pg_user: str
    pg_name: str
    pg_password: str
    pg_host: str
    pg_port: int

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
        return f"postgresql+psycopg://{self.postgres.pg_user}:{self.postgres.pg_password}@{self.postgres.pg_host}:{str(self.postgres.pg_port)}/{str(self.postgres.pg_name)}"


THIS_DIR = Path(__file__).parent


def load_yaml(*paths: Path) -> dict[str, any]:
    config: dict[str, any] = {}

    for path in paths:
        with Path(path).open("r") as f:
            sub_config = safe_load(f)
        if not isinstance(sub_config, dict):
            raise TypeError(
                f"Config file has no top-level mapping: {path}"
            )
        config = {**config, **sub_config}
    return config


settings = Settings.model_validate(load_yaml(
    Path("../../db.yaml"),
    Path("../secret.yaml"),
))
