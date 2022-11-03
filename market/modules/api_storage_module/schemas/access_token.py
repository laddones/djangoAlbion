from pydantic import BaseModel

from .user_schema import UserRole


class AccessTokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    role: UserRole = UserRole.USER


class RefreshAccessTokenSchema(BaseModel):
    refresh_token: str
