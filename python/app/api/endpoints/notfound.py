from fastapi import APIRouter

router = APIRouter()

@router.get("/404")
async def notfound():
    # Link not found page
    pass
