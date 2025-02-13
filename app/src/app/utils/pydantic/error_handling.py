from pydantic import BaseModel, Field
from typing import Any


class DefaultErrorResponseSchema(BaseModel):
    code: int = Field(description="Error code",)
    message: str = Field(description="Error description")
    detail: Any = Field(description="Error details")


class DetailDefaultErrorResponseSchema(BaseModel):
    context: Any = Field(description="Error context")
    service: str = Field(description="Service name")
    description: str = Field(description="Error description")