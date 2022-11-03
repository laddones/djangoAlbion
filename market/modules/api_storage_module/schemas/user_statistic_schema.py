from typing import Optional

from pydantic import BaseModel


class UserStatisticSchema(BaseModel):
    count_of_created_links: Optional[int] = 0
    count_of_invited_users: Optional[int] = 0
    links_skip: Optional[int] = 0
    links_send_to_block: Optional[int] = 0
    links_blocked: Optional[int] = 0
