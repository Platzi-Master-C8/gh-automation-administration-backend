from typing import Optional
from datetime import datetime

from sqlalchemy import Column, DateTime, sql
from sqlmodel import Field, SQLModel


class Auditor(SQLModel):
    """
    Class containing the common attributes for all entities.
    """

    active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=sql.func.now(),
        )
    )
    created_by: Optional[int] = Field(default=None)
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            onupdate=sql.func.now(),
        )
    )
    updated_by: Optional[int] = Field(default=None)
