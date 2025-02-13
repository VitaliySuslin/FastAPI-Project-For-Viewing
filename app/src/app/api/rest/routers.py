from fastapi import FastAPI

from app.src.app.api.rest.views import health
from app.src.app.api.rest.views import organizations


def add_rest_routers(app: FastAPI) -> None:
    app.include_router(health.router, prefix='')
    app.include_router(organizations.router, prefix='')
