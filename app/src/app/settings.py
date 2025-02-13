import logging
import os
from typing import Union

from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv() 

class Settings(BaseSettings):
    """
    Base settings

    Attributes:
        SERVICE_TOKEN (str): Temporary service token for authentication.
        DEBUG (bool): Flag to enable or disable debug mode.
        RELOAD (bool): Flag to enable or disable auto-reload of the application.
        NAME (str): Name of the FastAPI project.
        LOG_LEVEL (int): Logging level for the application.
        USE_JSON_LOG_FORMAT (bool): Flag to enable or disable JSON format for logs.
        API_PATH_PREF (str): Prefix for API paths.
        APP_HOST (str): Host address for the application.
        APP_PORT (int): Port number for the application.
        CORS_ORIGINS (list): List of allowed origins for CORS.
        POSTGRES_USER (str): Username for PostgreSQL database.
        POSTGRES_PASSWORD (str): Password for PostgreSQL database.
        POSTGRES_DB (str): Name of the PostgreSQL database.
        POSTGRES_HOST (str): Host address for the PostgreSQL database.
        POSTGRES_PORT (int): Port number for the PostgreSQL database.
        POSTGRES_ECHO (bool): Flag to enable or disable SQLAlchemy echo for PostgreSQL.
    """
    SERVICE_TOKEN: str

    DEBUG: bool
    RELOAD: bool
    NAME: str = 'FastAPI Project'
    LOG_LEVEL: int = logging.WARNING
    USE_JSON_LOG_FORMAT: bool = False
    API_PATH_PREF: str = '/api/v1'
    APP_HOST: str
    APP_PORT: int = 8000

    CORS_ORIGINS: list = [
        '*',
    ]

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_ECHO: bool = False

    class Config:
        env_file_encoding = 'utf-8'


class LocalSettings(Settings):
    """
    Local settings
    """

    DEBUG: bool = True
    RELOAD: bool = True
    APP_HOST: str = '0.0.0.0'

    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'owner'
    POSTGRES_DB:str = 'fastapi_project'
    POSTGRES_HOST: str = '127.0.0.1'
    POSTGRES_PORT: int = 5432
    POSTGRES_ECHO: bool = True


class WorkSettings(Settings):
    """
    Work settings
    """

    DEBUG: bool = False
    RELOAD: bool = False
    APP_HOST: str = '0.0.0.0'

    POSTGRES_USER: str = ''
    POSTGRES_PASSWORD: str = ''
    POSTGRES_DB:str = ''
    POSTGRES_HOST: str = ''
    POSTGRES_PORT: int = 0
    POSTGRES_ECHO: bool = False


def get_settings() -> Union[WorkSettings, LocalSettings]:
    env_type = os.environ['ENV_TYPER']
    config_cls_dict = {
        'local': LocalSettings,
        'work': WorkSettings
    }
    config_cls = config_cls_dict[env_type]
    return config_cls()


settings = get_settings()