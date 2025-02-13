from pydantic import BaseModel, Field
from datetime import datetime


class BuildingSchema(BaseModel):
    id: int = Field(..., title="Unique identifier of the building")
    address: str = Field(..., title="Address of the building")
    latitude: float = Field(..., title="Geographical latitude of the building")
    longitude: float = Field(..., title="Geographical longitude of the building")

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }