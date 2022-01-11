from typing import Optional

from pydantic import BaseModel, Field


class RoleBase(BaseModel):
    """
    Class containing shared properties of the role.
    """

    role_name: str = Field(
        ...,
        max_length=50,
        title="Role Name",
        description="Name of the role",
        example="Administrator",
    )
    role_description: Optional[str] = Field(
        min_length=5,
        title="Role Description",
        description="Description of the role",
        example="Administrator",
    )


class RoleCreate(RoleBase):
    """
    Class containing properties to create a new role.
    """
    pass


class RoleUpdate(RoleBase):
    """
    Class containing properties to update an existing role.
    """
    role_name: Optional[str] = Field(
        max_length=50,
        title="Role Name",
        description="Name of the role",
        example="Administrator",
    )


class Role(RoleBase):
    """
    Class containing properties to retrieve a role to the client.
    """
    role_id: int = Field(
        ...,
        title="Role ID",
        description="Unique identifier of the role.",
        example=1,
    )
