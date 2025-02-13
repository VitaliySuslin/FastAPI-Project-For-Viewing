from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.activity import ActivityModel
from app.src.app.utils.pydantic.error_handling import DefaultErrorResponseSchema, DetailDefaultErrorResponseSchema
from app.src.app.settings import settings


async def check_activity_exists(
    activity_id: int,
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> int:
    activity_query = await session.execute(
        select(ActivityModel).where(ActivityModel.id == activity_id)
    )
    activity = activity_query.scalar_one_or_none()

    if not activity:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10004,
                message="Activity ID not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Activity ID not found"},
                    service=settings.NAME,
                    description="The specified activity does not exist"
                )
            ).dict()
        )
    return activity_id