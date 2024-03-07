from datetime import date
from typing import Optional, List

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

app = FastAPI()


class HotelsArgs:
    def __init__(
            self,
            location: str,
            date_from: str,
            date_to: str,
            stars: Optional[int] = Query(default=None, ge=1, le=5),
            has_spa: Optional[bool] = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


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
async def hotels(search_args: HotelsArgs = Depends()):
    return [search_args]


@app.post("/register")
async def register_user(
        user: Sregister
):
    return user
