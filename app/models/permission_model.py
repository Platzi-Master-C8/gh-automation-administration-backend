from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import Column, String
from sqlmodel import Field, Relationship

from app.models import Auditor


if TYPE_CHECKING:
    from app.models import RoleHasPermission
    from app.models import Role


class Permission(Auditor, table=True):
    """
    Class representing a permission in database.
    """
    permission_id: Optional[int] = Field(default=None, primary_key=True)
    permission_name: str = Field(
        ...,
        sa_column=Column(
            "permission_name",
            String(50),
            unique=True,
        )
    )
    permission_description: Optional[str] = Field(default=False)
    roles: List["Role"] = Relationship(
        back_populates="permissions",
        link_model=RoleHasPermission,
    )
