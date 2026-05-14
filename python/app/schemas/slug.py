from pydantic import BaseModel

class SlugFromUser(BaseModel):
    slug: str