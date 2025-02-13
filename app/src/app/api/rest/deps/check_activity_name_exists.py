from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.activity import ActivityModel
from app.src.app.utils.pydantic.error_handling import DefaultErrorResponseSchema, DetailDefaultErrorResponseSchema
from app.src.app.settings import settings


async def check_activity_name_exists(
    activity_name: str,
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> str:
    activity_query = await session.execute(
        select(ActivityModel).where(ActivityModel.name == activity_name)
    )
    activity = activity_query.scalar_one_or_none()

    if not activity:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10006,
                message="Activity name not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Activity name not found"},
                    service=settings.NAME,
                    description="The specified activity name does not exist"
                )
            ).dict()
        )
    return activity_name