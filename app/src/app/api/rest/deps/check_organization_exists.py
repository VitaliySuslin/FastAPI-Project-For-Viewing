from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.organization import OrganizationModel
from app.src.app.utils.pydantic.error_handling import DefaultErrorResponseSchema, DetailDefaultErrorResponseSchema
from app.src.app.settings import settings


async def check_organization_exists(
    organization_id: int,
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> int:
    organization_query = await session.execute(
        select(OrganizationModel).where(OrganizationModel.id == organization_id)
    )
    organization = organization_query.scalar_one_or_none()

    if not organization:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10005,
                message="Organization ID not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Organization ID not found"},
                    service=settings.NAME,
                    description="The specified organization does not exist"
                )
            ).dict()
        )
    return organization_id