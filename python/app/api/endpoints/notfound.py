from fastapi import APIRouter

router = APIRouter()

@router.get("/404")
async def notfound():
    return {"Hello": "NotFound"}
