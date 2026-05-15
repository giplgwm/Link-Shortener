from fastapi import APIRouter

router = APIRouter()

@router.get("/info/{slug}")
async def info(slug: str):
    # Return info about a shortened link
    pass