from fastapi import APIRouter
from sqlalchemy import text

from app.src.app.api.rest.schemas.responses.health import HealthSchema
from app.src.app.settings import settings

from app.src.app.enums.tools import HealthStatusType

from app.src.app.extensions.logging import logger
from app.src.app.extensions.sqlalchemy import PoolConnector


router = APIRouter(tags=["Tools Box"], prefix=settings.API_PATH_PREF)


class HealthController(object):
    @classmethod
    async def _connect_sql(cls):
        async with PoolConnector.session() as session:

            await session.execute(
                text("SELECT 1"),
            )

    @classmethod
    async def _check_sql(cls, health: HealthSchema):
        try:
            await cls._connect_sql()
        except Exception as exc:
            health.sql_status = HealthStatusType.error
            logger.error("sql health error {0}".format(str(exc)))
        else:
            health.sql_status = HealthStatusType.ok

    @classmethod
    async def create(cls) -> HealthSchema:
        health = HealthSchema()
        await cls._check_sql(health)
        return health


@router.get(
    "/tools/health",
    response_model_exclude_none=True,
    response_model=HealthSchema,
)
async def health_check() -> HealthSchema:
    return await HealthController.create()


@router.get(
    "/tools/error-response",
    response_model_exclude_none=True,
    response_model=HealthSchema,
)
async def health_check():
    1 / 0
