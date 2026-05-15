from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.schemas import SlugFromUser

router = APIRouter()

@router.get("/{slug}")
async def redirect(slug: SlugFromUser):
    # Redirect to original url
    original_url = None
    # if slug in db:
    return RedirectResponse(original_url, HTTPStatus.TEMPORARY_REDIRECT)
    # if slug not in db:
    return RedirectResponse("/404", HTTPStatus.TEMPORARY_REDIRECT)
