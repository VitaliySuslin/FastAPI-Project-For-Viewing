from fastapi import FastAPI

from app.src.app.api.urls import init_routers
from app.src.app.settings import settings
from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.middlewares.init_middlewares import add_middlewares


def make_app() -> FastAPI:
    app = FastAPI(
        title="Organizations API",
        debug=settings.DEBUG,
        docs_url=f"{settings.API_PATH_PREF}/docs",
        redoc_url=f"{settings.API_PATH_PREF}/redoc",
        openapi_url=f"{settings.API_PATH_PREF}/openapi.json",
    )

    add_middlewares(app)
    init_routers(app)
    PoolConnector()
    
    return app