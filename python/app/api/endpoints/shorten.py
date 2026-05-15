from fastapi import APIRouter, Request
from nanoid import generate
from app.schemas import LinkFromUser
from app.db import queries
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/shorten", status_code=201)
async def shorten(link: LinkFromUser, request: Request):
    url = str(link.link)
    forwarded = request.headers.get("X-Forwarded-For", "")
    created_by = forwarded.split(",")[0] if forwarded else request.client.host
    
    inserted = False
    for _ in range(5):
        slug = generate(size=8)
        try:
            print(f"inserting ${url} into db with slug ${slug}. Added by IP {created_by}")
            queries.insert_link(url=url, slug=slug, created_by=created_by)
        except IntegrityError:
            continue
    
    return { 'slug' : slug }