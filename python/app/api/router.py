from fastapi import APIRouter
from app.api.endpoints import info, notfound, redirect, root, shorten

router = APIRouter()

router.include_router(info.router)
router.include_router(notfound.router)
router.include_router(root.router)
router.include_router(shorten.router)
#Redirect comes last to make sure /{slug} does not take priority for matching over names routes
router.include_router(redirect.router)
