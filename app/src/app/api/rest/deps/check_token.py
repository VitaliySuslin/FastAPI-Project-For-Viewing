from typing import Optional

from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.src.app.settings import settings
from app.src.app.utils.pydantic.error_handling import (
    DetailDefaultErrorResponseSchema,
    DefaultErrorResponseSchema
)


async def check_token(
        auth: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
) -> None:
    if auth.credentials == settings.SERVICE_TOKEN:
        return
    raise HTTPException(
        status_code=401,
        detail=DefaultErrorResponseSchema(
            code=10001,
            message="Unauthorized",
            detail=DetailDefaultErrorResponseSchema(
                context={
                    "error": "Not valid token"
                },
                service=settings.NAME,
                description="Invalid token"
            )
        ).dict()
    )