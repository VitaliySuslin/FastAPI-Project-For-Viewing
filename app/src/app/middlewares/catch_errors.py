from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.src.app.middlewares.deps.get_last_trace import get_last_trace
from app.src.app.enums.error_code_response import ErrorCodeResponseEnum
from app.src.app.enums.services import AppNameEnum
from app.src.app.utils.pydantic.error_handling import DetailDefaultErrorResponseSchema, DefaultErrorResponseSchema


class SendDefaultErrorResponseByExceptionMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        try:
            response = await call_next(request)
        except Exception as err:

            return JSONResponse(
                status_code=500,
                content=DefaultErrorResponseSchema(
                    code=ErrorCodeResponseEnum.error_server_global,
                    message="Critical server error",
                    detail=DetailDefaultErrorResponseSchema(
                        context={
                            "err": str(err)[:500],
                            "trace": await get_last_trace(),
                        },
                        service=AppNameEnum.app,
                        description="The server dropped from 500",
                    ),
                ).model_dump(),
            )
        return response
