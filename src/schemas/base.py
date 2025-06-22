"""Модуль содержит основные переменные для работы бота."""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # fastapi
    FASTAPI_HOST: str
    FASTAPI_PORT: int

    # redis
    REDIS_URL: str
    
    # core
    LOG_LEVEL: str

    # telegram
    BOT_TOKEN: SecretStr
    CHANNEL_USERNAME: str
    CHANNEL_LINK: str
    REQUEST_LIMIT: int

    # openai
    OPENAI_API_KEY: str

    ROOT_DIR: Path = Path(__file__).resolve().parents[2]

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / '.env',
        env_file_encoding="utf-8"
    )


config = Config()
