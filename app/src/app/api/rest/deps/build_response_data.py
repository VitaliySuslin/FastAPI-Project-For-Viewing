from typing import List

from app.src.app.db.models.organization import OrganizationModel
from app.src.app.api.rest.schemas.responses.organizations_schemas import (
    OutOrganizationResponseSchema,
    PhoneNumberSchema,
    BuildingSchema,
    ActivitySchema
)


def build_response_data(organizations: List[OrganizationModel]) -> List[OutOrganizationResponseSchema]:
    return [
        OutOrganizationResponseSchema(
            id=org.id,
            name=org.name,
            phone_numbers=[PhoneNumberSchema.from_orm(pn) for pn in org.phone_numbers],
            building=BuildingSchema.from_orm(org.building) if org.building else None,
            activities=ActivitySchema.build_tree(org.activities)
        ) for org in organizations
    ]