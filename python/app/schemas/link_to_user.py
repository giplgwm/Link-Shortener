from pydantic import BaseModel

class LinkToUser(BaseModel):
    url: str
    slug: str
    