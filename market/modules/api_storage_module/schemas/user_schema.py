from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserSignUpRequestSchema(BaseModel):
    id: int
    first_name: str
    username: Optional[str] = None
    last_name: Optional[str] = None
    inviter_id: Optional[int] = None


class UserRole(str, Enum):
    OWNER = "owner"
    USER = "user"
    MODERATOR = "moderator"
    MAIN_MODERATOR = "main_moderator"
    BANNED = "banned"


class UserUpdateSchema(BaseModel):
    role: UserRole = UserRole.USER
    is_active: bool = False


class UserGlobalStatisticSchema(BaseModel):
    user_count: int = 0
    valid_user_count: int = 0
    user_with_report_count: int = 0
    user_with_added_links_count: int = 0
    user_with_inviters_count: int = 0


class UserSchema(BaseModel):
    id: int
    first_name: str
    role: UserRole = UserRole.USER
    is_active: bool = False
    username: Optional[str] = None
    last_name: Optional[str] = None
    inviter_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserDetailSchema(BaseModel):
    id: int
    first_name: str
    role: UserRole = UserRole.USER
    is_active: bool = False
    username: Optional[str] = None
    last_name: Optional[str] = None
    inviter_id: Optional[int] = None
    count_of_invited_users: int = 0
    count_of_links: int = 0
    blocker_position: int = 0
    inviter_position: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
