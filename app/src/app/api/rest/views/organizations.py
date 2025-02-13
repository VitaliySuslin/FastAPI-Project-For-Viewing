from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.src.app.extensions.sqlalchemy import PoolConnector
from app.src.app.db.models.organization import OrganizationModel
from app.src.app.db.models.activity import ActivityModel
from app.src.app.db.models.building import BuildingModel
from app.src.app.api.rest.deps.check_token import check_token
from app.src.app.api.rest.deps.check_building_exists import check_building_exists
from app.src.app.api.rest.deps.check_activity_exists import check_activity_exists
from app.src.app.api.rest.deps.check_activity_name_exists import check_activity_name_exists
from app.src.app.api.rest.deps.check_organization_exists import check_organization_exists
from app.src.app.api.rest.deps.check_organization_name_exists import check_organization_name_exists
from app.src.app.api.rest.schemas.responses.organizations_schemas import OutOrganizationResponseSchema
from app.src.app.api.rest.schemas.requests.organizations_schemas import LocationQuerySchema
from app.src.app.utils.pydantic.error_handling import (
    DefaultErrorResponseSchema,
    DetailDefaultErrorResponseSchema
)
from app.src.app.api.rest.deps.build_response_data import build_response_data
from app.src.app.api.rest.deps.execute_organization_query import execute_organization_query
from app.src.app.settings import settings


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.get("/by-building/{building_id}", dependencies=[Depends(check_token)], response_model=List[OutOrganizationResponseSchema])
async def get_organizations_by_building(
    building_id: int = Depends(check_building_exists),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> List[OutOrganizationResponseSchema]:
    organizations = await execute_organization_query(session, OrganizationModel.building_id == building_id)
    return build_response_data(organizations)

@router.get("/by-activity/{activity_id}", dependencies=[Depends(check_token)], response_model=List[OutOrganizationResponseSchema])
async def get_organizations_by_activity(
    activity_id: int = Depends(check_activity_exists),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> List[OutOrganizationResponseSchema]:
    organizations = await execute_organization_query(session, ActivityModel.id == activity_id)
    if not organizations:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10010,
                message="No organizations found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "No organizations found for this activity"},
                    service=settings.NAME,
                    description="Activity ID not found"
                )
            ).dict()
        )
    return build_response_data(organizations)

@router.get("/{organization_id}", dependencies=[Depends(check_token)], response_model=OutOrganizationResponseSchema)
async def get_organization_by_id(
    organization_id: int = Depends(check_organization_exists),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> OutOrganizationResponseSchema:
    organizations = await execute_organization_query(session, OrganizationModel.id == organization_id)
    if not organizations:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10011,
                message="Organization not found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "Organization not found"},
                    service=settings.NAME,
                    description="Organization ID not found"
                )
            ).dict()
        )
    return build_response_data(organizations)[0]

@router.get("/search-by-activity/{activity_name}", dependencies=[Depends(check_token)], response_model=List[OutOrganizationResponseSchema])
async def search_organizations_by_activity(
    activity_name: str = Depends(check_activity_name_exists),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> List[OutOrganizationResponseSchema]:
    organizations = await execute_organization_query(session, ActivityModel.name.ilike(f"%{activity_name}%"))
    if not organizations:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10012,
                message="No organizations found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "No organizations found for this activity"},
                    service=settings.NAME,
                    description="Activity name not found"
                )
            ).dict()
        )
    return build_response_data(organizations)

@router.get("/search-by-name/{name}", dependencies=[Depends(check_token)], response_model=List[OutOrganizationResponseSchema])
async def search_organizations_by_name(
    name: str = Depends(check_organization_name_exists),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> List[OutOrganizationResponseSchema]:
    organizations = await execute_organization_query(session, OrganizationModel.name.ilike(f"%{name}%"))
    if not organizations:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10013,
                message="No organizations found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "No organizations found with this name"},
                    service=settings.NAME,
                    description="Organization name not found"
                )
            ).dict()
        )
    return build_response_data(organizations)

@router.get("/geo/search-by-location", dependencies=[Depends(check_token)], response_model=List[OutOrganizationResponseSchema])
async def search_organizations_by_location(
    location: LocationQuerySchema = Depends(),
    session: AsyncSession = Depends(PoolConnector.get_session)
) -> List[OutOrganizationResponseSchema]:
    organizations = await execute_organization_query(
        session,
        (BuildingModel.latitude.between(location.latitude - location.radius, location.latitude + location.radius)) &
        (BuildingModel.longitude.between(location.longitude - location.radius, location.longitude + location.radius))
    )
    if not organizations:
        raise HTTPException(
            status_code=400,
            detail=DefaultErrorResponseSchema(
                code=10014,
                message="No organizations found",
                detail=DetailDefaultErrorResponseSchema(
                    context={"error": "No organizations found in the specified location"},
                    service=settings.NAME,
                    description="No organizations found within the specified radius"
                )
            ).dict()
        )
    return build_response_data(organizations)