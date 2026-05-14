from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from http import HTTPStatus
import sqlite3

app = FastAPI()

