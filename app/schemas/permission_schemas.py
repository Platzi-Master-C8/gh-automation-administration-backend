from typing import Optional

import pydantic
from pydantic import BaseModel, Field


PermissionNameType = pydantic.constr(regex="^can-(read|write)-(any|own)-.+$")


class PermissionBase(BaseModel):
    """
    Class containing shared properties of the permission.
    """
    permission_name: PermissionNameType = Field(
        ...,
        max_length=50,
        title="Permission Name",
        description="Name of the permission",
        example="can-write-any-users",
    )
    permission_description: Optional[str] = Field(
        min_length=5,
        title="Permission Description",
        description="Description of the permission",
        example="Total control over users",
    )


class PermissionCreate(PermissionBase):
    """
    Class containing properties to create a new permission.
    """
    pass


class PermissionUpdate(PermissionBase):
    """
    Class containing properties to update an existing permission.
    """
    permission_name: Optional[PermissionNameType] = Field(
        max_length=50,
        title="Permission Name",
        description="Name of the permission",
        example="Administrator",
    )


class Permission(PermissionBase):
    """
    Class containing properties to retrieve a permission to the client.
    """
    permission_id: int = Field(
        ...,
        title="Permission ID",
        description="Unique identifier of the permission.",
        example=1,
    )
