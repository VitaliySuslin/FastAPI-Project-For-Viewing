from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.src.app.middlewares.catch_errors import SendDefaultErrorResponseByExceptionMiddleware


def add_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(
        SendDefaultErrorResponseByExceptionMiddleware,
    )
