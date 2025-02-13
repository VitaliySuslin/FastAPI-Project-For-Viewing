from pydantic import BaseModel
from typing import List, Optional


class PhoneNumberSchema(BaseModel):
    id: int
    number: str
    organization_id: int

    class Config:
        from_attributes = True


class BuildingSchema(BaseModel):
    id: int
    address: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class ActivitySchema(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    children: List['ActivitySchema'] = []

    class Config:
        from_attributes = True

    @classmethod
    def build_tree(cls, activities):
        activity_map = {activity.id: cls.from_orm(activity) for activity in activities}
        root_activities = []

        for activity in activities:
            if activity.parent_id is None:
                root_activities.append(activity_map[activity.id])
            else:
                parent = activity_map.get(activity.parent_id)
                if parent:
                    parent.children.append(activity_map[activity.id])

        return root_activities


class OutOrganizationResponseSchema(BaseModel):
    id: int
    name: str
    phone_numbers: List[PhoneNumberSchema]
    building: Optional[BuildingSchema]
    activities: List[ActivitySchema]

    class Config:
        from_attributes = True


ActivitySchema.update_forward_refs()