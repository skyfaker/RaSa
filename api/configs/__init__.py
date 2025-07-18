from pydantic_settings import SettingsConfigDict

from .middleware_config import MiddlewareConfig
from .log_config import LogConfig


class AppConfig(LogConfig, MiddlewareConfig):
    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file=".env",
        env_file_encoding="utf-8",
        # ignore extra attributes
        extra="ignore",
    )


app_config = AppConfig()

__all__ = ["app_config"]
