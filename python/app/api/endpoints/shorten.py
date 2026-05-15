from fastapi import APIRouter, Request
from nanoid import generate
from app.schemas import LinkFromUser
from app.db import queries

router = APIRouter()

@router.post("/shorten")
async def shorten(link: LinkFromUser, request: Request):
    slug = generate(size=8)
    forwarded = request.headers.get("X-Forwarded-For")
    created_by = forwarded.split(",")[0] if forwarded else request.client.host
    queries.insert_link(url=str(link), slug=slug, created_by=created_by)
    return { 'slug' : slug }