from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class OrganizationSchema(BaseModel):
    id: int = Field(..., title="Unique identifier of the organization")
    name: str = Field(..., title="Name of the organization", max_length=100)
    phone_numbers: List[str] = Field(..., title="List of phone numbers of the organization", max_items=5)
    building_id: int = Field(..., title="ID of the building where the organization is located")
    activities: List[int] = Field(..., title="List of activity IDs that the organization is involved in")
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }