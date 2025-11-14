from typing import Optional

from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        env_file: str = ".env"


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
