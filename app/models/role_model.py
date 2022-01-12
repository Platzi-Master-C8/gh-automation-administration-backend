from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import Column, String
from sqlmodel import Field, Relationship

from app.models import Auditor


if TYPE_CHECKING:
    from app.models import RoleHasPermission
    from app.models import Permission
    from app.models import User


class Role(Auditor, table=True):
    """
    Class representing a role in database.
    """
    role_id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str = Field(
        ...,
        sa_column=Column(
            "role_name",
            String(50),
            nullable=False,
            unique=True,
        )
    )
    role_description: Optional[str] = Field(default=None)
    users: List["User"] = Relationship(back_populates="role")
    permissions: List["Permission"] = Relationship(
        back_populates="roles",
        link_model=RoleHasPermission
    )
