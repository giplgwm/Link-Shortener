# Python

## Run app
1. Clone repo `git clone https://github.com/giplgwm/Link-Shortener.git`
1. Open link shortener/python directory `cd Link-Shortener/python`
1. Create and activate virtual environment `python -m venv .venv && . ./.venv/bin/activate`
1. Install requirements `pip install -r requirements.txt`
1. Run fastapi dev server `fastapi dev app/app.py`
1. Navigate to localhost:8000/

## Libraries used
- fastapi - webapi framework
- pigsql - handles parameterized sql statements without a full ORM
- nanoid - generates slugs

## File Structure:
- /api/endpoints - routes
- /db/queries - sql queries for pigsql
- /schemas - Pydantic models for input/output validation
