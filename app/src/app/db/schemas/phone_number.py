from pydantic import BaseModel
from datetime import datetime


class PhoneNumberSchema(BaseModel):
    id: int
    number: str
    organization_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }