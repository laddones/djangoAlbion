from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LinkActionEnum(str, Enum):
    SKIPPED = "skipped"
    ALREADY_BLOCKED = "already_blocked"
    BLOCK_REPORT = "block_report"


class LinkTypeEnum(str, Enum):
    YOUTUBE = 'youtube'
    TWITTER = 'twitter'
    TELEGRAM = 'telegram'
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    TIKTOK = 'tiktok'
    OTHER = 'other'
    MEMBER = 'member'
    PERMITTED = 'permitted'
    FAKE_BOT = 'fake_bot'


class LinkStatusSchema(str, Enum):
    PROCESSING = "processing"
    SUBMITTED = "submitted"
    DELETED = "deleted"
    PUBLISHED = "published"
    BLOCKED = "blocked"


class LinkCategoryEnum(str, Enum):
    RESTRAINED_INFORMATION = "restrained_information"
    AGGRESSIVE_INFORMATION = "aggressive_information"
    RESTRAINED_MILITARY = "restrained_military"
    AGGRESSIVE_MILITARY = "aggressive_military"
    UNRECOGNIZED_REPUBLICS = "unrecognized_republics"
    COORDINATION_OF_ATTACKS = "coordination_of_attacks"
    CYBER_ATTACK_COORDINATION = "cyber_attack_coordination"


class AdminCreateLinkSchema(BaseModel):
    link: str
    link_category: Optional[LinkCategoryEnum] = None
    description: Optional[str] = None
    link_type: LinkTypeEnum = LinkTypeEnum.OTHER


class AdminUpdateLinkSchema(BaseModel):
    link: Optional[str] = None
    link_category: Optional[LinkCategoryEnum] = None
    description: Optional[str] = None
    link_type: Optional[LinkTypeEnum] = None
    link_status: Optional[LinkStatusSchema] = None


class CreateLinkSchema(BaseModel):
    link: str
    description: Optional[str] = None
    link_type: LinkTypeEnum = LinkTypeEnum.OTHER


class LinkActionSchema(BaseModel):
    link_action: LinkActionEnum


class LinkDetailSchema(BaseModel):
    id: int
    link: str
    added_by_id: int
    link_type: LinkTypeEnum = LinkTypeEnum.OTHER
    link_status: LinkStatusSchema = LinkStatusSchema.PROCESSING
    link_action: Optional[LinkActionEnum] = None
    link_category: Optional[LinkCategoryEnum] = None
    description: Optional[str] = None
    count_of_blocked: int = 0
    count_of_report: int = 0

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class LinkUpdateTypeEnum(str, Enum):
    UPDATE = "update"
    CREATE = "create"
    REMOVE = "remove"


class UserOrderByParameterApiEnum(str, Enum):
    COUNT_OF_BLOCKED = "count_of_blocked"
    COUNT_OF_INVITED = "count_of_invited"


class LinkUpdateSchema(BaseModel):
    link_update_type: LinkUpdateTypeEnum
    user_id: int
    link_id: int
    created_at: Optional[datetime] = None
    id: Optional[int] = None

