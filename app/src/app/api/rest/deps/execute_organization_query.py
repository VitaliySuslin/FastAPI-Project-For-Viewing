from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.src.app.db.models.organization import OrganizationModel
from app.src.app.db.models.activity import ActivityModel


async def execute_organization_query(
    session: AsyncSession,
    where_clause
) -> List[OrganizationModel]:
    org_query = await session.execute(
        select(OrganizationModel)
        .options(
            joinedload(OrganizationModel.phone_numbers),
            joinedload(OrganizationModel.building),
            joinedload(OrganizationModel.activities).joinedload(ActivityModel.sub_activities)
        )
        .where(where_clause)
    )
    return org_query.scalars().unique().all()