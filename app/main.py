import uvicorn
from fastapi import FastAPI

from app.src.app.settings import settings
from app.src.app.factory import make_app

app: FastAPI = make_app()

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        debug=settings.DEBUG,
        reload=settings.RELOAD,
    )
