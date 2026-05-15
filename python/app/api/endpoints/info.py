from fastapi import APIRouter, HTTPException
from app.db import queries
from app.schemas import LinkToUser
from http import HTTPStatus

router = APIRouter()

@router.get("/info/{slug}", response_model=LinkToUser)
async def info(slug: str):
    result = queries.get_link_info(slug=slug)
    if result:
        return result
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Link not found")