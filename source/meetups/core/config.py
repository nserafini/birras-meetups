from functools import lru_cache

from pydantic import BaseSettings
from pydantic import root_validator


class BaseConfig(BaseSettings):

    API_NAME: str = "Meetups"
    API_VERSION: str = "1"
    TIMEZONE: str = "America/Buenos_Aires"
    LOG_LEVEL: str = "INFO"
    POSTGRES_HOST: str = ""
    POSTGRES_PORT: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_NAME: str = ""
    POSTGRES_DSN: str = ""

    @root_validator()
    def dsn(cls, values):
        dsn = values.get("POSTGRES_DSN")
        if not dsn:
            host = values["POSTGRES_HOST"]
            port = values.get("POSTGRES_PORT", "")
            endpoint = host + (f":{port}" if port else "")
            user = values.get("POSTGRES_USER", "")
            password = values.get("POSTGRES_PASSWORD", "")
            credentials = user + (f":{password}" if password else "")
            name = values["POSTGRES_NAME"]
            dsn = f"postgresql://{credentials}@{endpoint}/{name}"
            values["POSTGRES_DSN"] = dsn
        return values

@lru_cache()
def get_api_settings() -> BaseConfig:
    return BaseConfig()


settings = get_api_settings()
