from pydantic import BaseModel

class LinkToUser(BaseModel):
    link: str
    slug: str
    