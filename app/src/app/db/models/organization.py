from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.src.app.extensions.sqlalchemy import Base
from app.src.app.utils.sqlalchemy.base_model_mixin import (
    BaseTimeColumnModelMixin,
    BaseModelMixin
)

if TYPE_CHECKING:
    from app.src.app.db.models.building import BuildingModel
    from app.src.app.db.models.phone_number import PhoneNumberModel
    from app.src.app.db.models.activity import ActivityModel


class OrganizationModel(Base, BaseTimeColumnModelMixin, BaseModelMixin):
    __tablename__ = 'organizations'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String, nullable=False)
    building_id = Column(Integer, ForeignKey('buildings.id'), nullable=False)

    # Связь с building
    building: Mapped["BuildingModel"] = relationship("BuildingModel", back_populates="organizations")

    # Связь с phone_numbers
    phone_numbers: Mapped[List["PhoneNumberModel"]] = relationship("PhoneNumberModel", back_populates="organization")

    # Связь с activities
    activities: Mapped[List["ActivityModel"]] = relationship("ActivityModel", back_populates="organization")