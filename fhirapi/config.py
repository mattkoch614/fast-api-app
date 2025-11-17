from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None

    class Config:
        env_file: str = ".env"
        extra = "ignore"  # Ignore extra fields when reading .env file


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(GlobalConfig):
    class Config:
        env_prefix: str = "DEV_"


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True

    class Config:
        env_prefix: str = "TEST_"


class ProdConfig(GlobalConfig):
    class Config:
        env_prefix: str = "PROD_"


@lru_cache()
def get_config(env_state: Optional[str]):
    configs = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
    env_state = env_state or "dev"  # Default to "dev" if not set
    return configs[env_state.lower()]()


config = get_config(BaseConfig().ENV_STATE)
