from enum import Enum


class HealthStatusType(str, Enum):
    ok = 'ok'
    error = 'error'