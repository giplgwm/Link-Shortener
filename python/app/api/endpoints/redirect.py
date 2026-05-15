from fastapi import APIRouter

router = APIRouter()

@router.get("/{slug}")
async def redirect(slug: str):
    # Redirect to original url
    pass
    # if slug in db:
        return RedirectResponse(original_url, HTTPStatus.TEMPORARY_REDIRECT)
    # if slug not in db:
        return RedirectResponse("/404", HTTPStatus.TEMPORARY_REDIRECT)
