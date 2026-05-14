from fastapi import FastAPI, APIRouter

from app.api import APIrouter

router = APIRouter()
router.include_router(APIrouter)

app = FastAPI()

