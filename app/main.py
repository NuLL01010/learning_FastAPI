from datetime import date
from typing import Optional, List

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Shotels(BaseModel):
    location: str
    date_from: str
    date_to: str
    stars: Optional[int] = Query(default=None, ge=1, le=5)
    has_spa: Optional[bool] = None


class Sregister(BaseModel):
    login: str
    email: str
    password: str
    age: Optional[int] = None


@app.get("/hotels")
async def hotels(
        location: str,
        date_from: str,
        date_to: str,
        stars: Optional[int] = Query(default=None, ge=1, le=5),
        has_spa: Optional[bool] = None
) -> List[Shotels]:
    return [
        {
            "location": location,
            "date_from": date_from,
            "date_to": date_to,
            "stars": stars,
            "has_spa": has_spa
        }
    ]


@app.post("/register")
async def register_user(
        user: Sregister
):
    return user
