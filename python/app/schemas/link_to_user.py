from pydantic import BaseModel

class LinkToUser(BaseModel):
    url: str
    slug: str
    created_by: str
    created_at: int
    clicks: int
    