from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "frontend"


@router.get("/404")
async def notfound():
    return FileResponse(FRONTEND_DIR / "404.html", media_type="text/html")
