from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List

from app.src.app.extensions.sqlalchemy import Base
from app.src.app.utils.sqlalchemy.base_model_mixin import (
    BaseTimeColumnModelMixin,
    BaseModelMixin
)

if TYPE_CHECKING:
    from app.src.app.db.models.organization import OrganizationModel


class ActivityModel(Base, BaseTimeColumnModelMixin, BaseModelMixin):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('activities.id'), nullable=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)

    organization: Mapped["OrganizationModel"] = relationship("OrganizationModel", back_populates="activities")

    sub_activities: Mapped[List["ActivityModel"]] = relationship(
        "ActivityModel",
        backref='parent',
        remote_side=[id]
    )