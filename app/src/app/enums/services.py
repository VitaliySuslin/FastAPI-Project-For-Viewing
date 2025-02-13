from enum import Enum

from app.src.app.settings import settings

class AppNameEnum(str, Enum):
    app = settings.NAME
