from pydantic import BaseModel


class LocationQuerySchema(BaseModel):
    latitude: float
    longitude: float
    radius: float