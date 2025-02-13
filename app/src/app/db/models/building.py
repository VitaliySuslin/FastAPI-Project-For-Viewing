from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.src.app.extensions.sqlalchemy import Base
from app.src.app.utils.sqlalchemy.base_model_mixin import (
    BaseTimeColumnModelMixin,
    BaseModelMixin
)

if TYPE_CHECKING:
    from app.src.app.db.models.organization import OrganizationModel


class BuildingModel(Base, BaseTimeColumnModelMixin, BaseModelMixin):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(primary_key=True)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Связь с организациями
    organizations: Mapped[List["OrganizationModel"]] = relationship("OrganizationModel", back_populates="building")