from typing import List, Optional

from sqlalchemy import Column, String
from sqlmodel import Field, Relationship, SQLModel

from app.models import Auditor


class RolePermission(SQLModel, table=True):
    """
    Class representing a pivot table between roles and permissions.
    """
    __tablename__ = 'roles_permissions'
    permission_id: Optional[int] = Field(
        default=None,
        foreign_key="permissions.permission_id",
        primary_key=True,
    )
    role_id: Optional[int] = Field(
        default=None,
        foreign_key="roles.role_id",
        primary_key=True,
    )


class Permission(Auditor, table=True):
    """
    Class representing a permission in database.
    """
    __tablename__ = 'permissions'
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
        link_model=RolePermission,
    )


class Role(Auditor, table=True):
    """
    Class representing a role in database.
    """
    __tablename__ = 'roles'
    role_id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str = Field(
        ...,
        sa_column=Column(
            "role_name",
            String(50),
            unique=True,
        )
    )
    role_description: Optional[str] = Field(default=None)
    users: List["User"] = Relationship(back_populates="role")
    permissions: List["Permission"] = Relationship(
        back_populates="roles",
        link_model=RolePermission,
    )


class User(Auditor, table=True):
    """
    Class representing a user in database.
    """
    __tablename__ = 'users'
    user_id: Optional[int] = Field(default=None, primary_key=True)
    role_id: Optional[int] = Field(default=2, foreign_key="roles.role_id")
    name: Optional[str] = Field(default=None)
    email: str = Field(
        sa_column=Column(
            "email",
            String(50),
            unique=True,
        )
    )
    password: str = Field(..., max_length=64)
    role: Optional["Role"] = Relationship(back_populates="users")
