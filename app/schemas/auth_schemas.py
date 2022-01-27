from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str = Field(
        title="Access Token",
        description="JWT access token",
        example="xxxxx.yyyyy.zzzzz",
    )
    token_type: str = Field(
        title="Token Type",
        description="Type of the token",
        example="bearer",
    )
