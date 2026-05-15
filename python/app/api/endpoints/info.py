from fastapi import APIRouter
from app.schemas import SlugFromUser

router = APIRouter()

@router.get("/info/{slug}")
async def info(slug: SlugFromUser):
    # Return info about a shortened link
    pass