from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/{slug}")
async def redirect(slug: str):
    # Redirect to original url
    pass
    # if slug in db:
    original_url = None
    return RedirectResponse(original_url, HTTPStatus.TEMPORARY_REDIRECT)
    # if slug not in db:
    return RedirectResponse("/404", HTTPStatus.TEMPORARY_REDIRECT)
