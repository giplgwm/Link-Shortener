from fastapi import APIRouter
from app.api.endpoints import info, notfound, redirect, root, shorten

APIrouter = APIRouter()

# APIrouter.include_router(info.router)
# APIrouter.include_router(notfound.router)
APIrouter.include_router(root.router)
APIrouter.include_router(shorten.router)
# # Redirect comes last to make sure /{slug} does not take priority for matching over named routes
# APIrouter.include_router(redirect.router)
