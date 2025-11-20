from functools import lru_cache
from typing import Optional

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",  # Ignore extra fields when reading .env file
    )


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    MAILGUN_API_KEY: Optional[str] = None
    MAILGUN_DOMAIN: Optional[str] = None
    LOGTAIL_API_KEY: Optional[str] = None
    B2_KEY_ID: Optional[str] = None
    B2_APPLICATION_KEY: Optional[str] = None
    B2_BUCKET_NAME: Optional[str] = None
    DEEPAI_API_KEY: Optional[str] = None


class DevConfig(GlobalConfig):
    model_config = ConfigDict(env_file=".env", extra="ignore", env_prefix="DEV_")


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True

    model_config = ConfigDict(env_file=".env", extra="ignore", env_prefix="TEST_")


class ProdConfig(GlobalConfig):
    model_config = ConfigDict(env_file=".env", extra="ignore", env_prefix="PROD_")


@lru_cache()
def get_config(env_state: Optional[str]):
    configs = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
    env_state = env_state or "dev"  # Default to "dev" if not set
    return configs[env_state.lower()]()


config = get_config(BaseConfig().ENV_STATE)
