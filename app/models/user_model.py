from typing import Optional
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
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
    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
        )
    )
    created_by: Optional[int] = Field(default=None)
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            onupdate=func.now(),
        )
    )
    updated_by: Optional[int] = Field(default=None)
