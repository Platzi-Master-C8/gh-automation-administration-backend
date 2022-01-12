from typing import Optional

from sqlmodel import Field, SQLModel


class RoleHasPermission(SQLModel, table=True):
    """
    Class representing a pivot table between roles and permissions.
    """
    permission_id: Optional[int] = Field(
        default=None,
        foreign_key="permission.id",
        primary_key=True,
    )
    role_id: Optional[int] = Field(
        default=None,
        foreign_key="role.id",
        primary_key=True,
    )
