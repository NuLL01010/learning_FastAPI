from datetime import date
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/hotels")
async def hotel(
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(default=None, ge=1, le=5),
        has_spa: Optional[bool] = None
):
    return location, date_from, date_to, stars, has_spa
