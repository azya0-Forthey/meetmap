from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from yaml import safe_load


class Server(BaseModel):
    server_port: int


class Postgres(BaseModel):
    pg_user: str
    pg_name: str
    pg_password: str
    pg_host: str
    pg_port: int


class Settings(BaseSettings):
    server: Server
    postgres: Postgres

    @property
    def get_psycopg_url(self):
        return f"postgresql+psycopg://{self.postgres.user}:{self.postgres.password}@{self.postgres.host}:{str(self.postgres.port)}/{str(self.postgres.name)}"

    model_config = SettingsConfigDict(yaml_file="../config.yaml")

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
    Path("../config.yaml"),
    Path("../../db.yaml")
))