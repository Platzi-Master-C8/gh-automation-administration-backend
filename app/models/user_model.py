from typing import Optional, TYPE_CHECKING

from sqlalchemy import Column, String
from sqlmodel import Field, Relationship

from app.models import Auditor


if TYPE_CHECKING:
    from app.models import Role


class User(Auditor, table=True):
    """
    Class representing a user in database.
    """
    user_id: Optional[int] = Field(default=None, primary_key=True)
    role_id: Optional[int] = Field(default=2, foreign_key="role.role_id")
    name: Optional[str] = Field(default=None)
    email: str = Field(
        sa_column=Column(
            "email",
            String(50),
            nullable=False,
            unique=True,
        )
    )
    password: str = Field(..., max_length=64)
    role: Optional["Role"] = Relationship(back_populates="users")
