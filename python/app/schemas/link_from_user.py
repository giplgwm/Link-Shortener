from pydantic import BaseModel, HttpUrl

class LinkFromUser(BaseModel):
    link: HttpUrl