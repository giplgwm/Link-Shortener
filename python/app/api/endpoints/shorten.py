from fastapi import APIRouter
from app.schemas import LinkFromUser

router = APIRouter()

@router.post("/shorten")
async def shorten(link: LinkFromUser):
    # Shorten link and return slug/shortlink for user to share
    pass
