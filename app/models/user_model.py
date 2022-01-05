from typing import Optional

from sqlalchemy import Column, String
from sqlmodel import Field

from app.models import Auditor


class User(Auditor, table=True):
    """
    Class representing a user in database.
    """

    user_id: Optional[int] = Field(default=None, primary_key=True)
    role_id: Optional[int] = Field(default=2)
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
