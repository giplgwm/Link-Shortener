from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.db import queries

router = APIRouter()

@router.get("/{slug}")
async def redirect(slug: str):
    original_url = queries.get_link(slug=slug)
    if original_url:
        queries.increment_clicks(slug=slug)
        return RedirectResponse(original_url['url'], HTTPStatus.FOUND)
    else:
        return RedirectResponse("/404", HTTPStatus.NOT_FOUND)
