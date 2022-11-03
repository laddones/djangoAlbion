from pydantic import BaseModel


class GlobalLinkStatisticSchema(BaseModel):
    count_of_links: int = 0
    count_of_link_in_processing: int = 0
    count_of_blocked_link: int = 0
    count_of_published: int = 0
