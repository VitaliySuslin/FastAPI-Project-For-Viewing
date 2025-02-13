from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ActivitySchema(BaseModel):
    id: int = Field(..., title="Unique identifier of the activity")
    name: str = Field(..., title="Name of the activity")
    parent_id: Optional[int] = Field(None, title="ID of the parent activity, if any")

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }