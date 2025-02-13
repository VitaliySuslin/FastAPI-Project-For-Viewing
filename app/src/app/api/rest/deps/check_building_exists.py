from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.building import BuildingModel
from app.src.app.utils.pydantic.error_handling import DefaultErrorResponseSchema, DetailDefaultErrorResponseSchema
from app.src.app.settings import settings


async def check_building_exists(
    building_id: int,
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> int:
    building_query = await session.execute(
        select(BuildingModel).where(BuildingModel.id == building_id)
    )
    building = building_query.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10003,
                message="Building ID not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Building ID not found"},
                    service=settings.NAME,
                    description="The specified building does not exist"
                )
            ).dict()
        )
    return building_id