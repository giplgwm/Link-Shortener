from fastapi import APIRouter

router = APIRouter()

@router.post("/shorten")
async def shorten(link: LinkFromUser):
    # Shorten link and return slug/shortlink for user to share
    pass
