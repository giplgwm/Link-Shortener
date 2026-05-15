from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    # Return home page
    pass
