from datetime import date
from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Sregister(BaseModel):
    login: str
    email: str
    password: str
    age: Optional[int] = None


@app.get("/hotels")
async def hotels(
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(default=None, ge=1, le=5),
        has_spa: Optional[bool] = None
):
    return location, date_from, date_to, stars, has_spa


@app.post("/register")
async def register_user(
    user: Sregister
):
    return user
