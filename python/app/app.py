from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from app.api import APIrouter
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('initializing database...')
    init_db()
    print('...server ready')
    yield
    


router = APIRouter()
router.include_router(APIrouter)

app = FastAPI()
app.include_router(router=router)
