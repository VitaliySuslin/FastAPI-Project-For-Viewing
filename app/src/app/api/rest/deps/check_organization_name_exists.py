from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.organization import OrganizationModel
from app.src.app.utils.pydantic.error_handling import DefaultErrorResponseSchema, DetailDefaultErrorResponseSchema
from app.src.app.settings import settings


async def check_organization_name_exists(
    name: str,
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> str:
    organization_query = await session.execute(
        select(OrganizationModel).where(OrganizationModel.name == name)
    )
    organization = organization_query.scalar_one_or_none()

    if not organization:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10007,
                message="Organization name not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Organization name not found"},
                    service=settings.NAME,
                    description="The specified organization name does not exist"
                )
            ).dict()
        )
    return name