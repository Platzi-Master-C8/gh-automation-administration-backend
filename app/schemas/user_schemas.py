from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """
    Class containin shared properties.
    """

    user_id: Optional[int] = Field(
        title="User ID",
        description="Unique identifier of the user.",
        example=1,
    )
    role_id: Optional[int] = Field(
        title="Role ID",
        description="Unique identifier of the role.",
        example=2,
    )
    name: Optional[str] = Field(
        max_length=50,
        title="User Name",
        description="Name of the user",
        example="John Doe",
    )
    email: Optional[EmailStr] = Field(
        title="Email",
        description="Email address of the user.",
        example="john@doe.com",
    )


class UserCreate(BaseModel):
    """
    Class containing properties for creating a new user.
    """

    email: EmailStr = Field(
        ...,
        title="Email",
        description="Email address of the user.",
        example="john@doe.com",
    )
    password: str = Field(
        ...,
        min_length=6,
        max_length=32,
        title="User Password",
        description="Password of the user",
        example="secret",
    )


class UserUpdate(UserBase):
    """
    Class containing properties for creating a new user.
    """

    password: Optional[str] = Field(
        min_length=6,
        max_length=32,
        title="User Password",
        description="Password of the user",
        example="secret",
    )


class User(UserBase):
    """
    Class containing properties for retrieveing to client.
    """

    pass
