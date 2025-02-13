from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.src.app.extensions.sqlalchemy import Base
from app.src.app.utils.sqlalchemy.base_model_mixin import (
    BaseTimeColumnModelMixin,
    BaseModelMixin
)

if TYPE_CHECKING:
    from app.src.app.db.models.organization import OrganizationModel


class PhoneNumberModel(Base, BaseTimeColumnModelMixin, BaseModelMixin):
    __tablename__ = 'phone_numbers'

    id: Mapped[int] = mapped_column(primary_key=True)
    number = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)

    # Связь с organization
    organization: Mapped["OrganizationModel"] = relationship("OrganizationModel", back_populates="phone_numbers")