from typing import Optional

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.images.router import router as router_images
from app.pages.router import router as router_pages
from app.hotels.router import router as router_hotels
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.rooms.router import router as router_rooms

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
# from fastapi_cache.decorator import cache

from redis import asyncio as aioredis


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")


app.include_router(router_users)
app.include_router(router_bookings) #  uvicorn app.main:app --reload
app.include_router(router_hotels)
app.include_router(router_rooms)

app.include_router(router_pages)
app.include_router(router_images)


# origins = [
# 	"https://localhost:3000",
# ]

# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=origins,
# 	allow_credentails=True,
# 	allow_methods=["GET", "POST", "DELETE", "PUT", "PUTH", "OPTIONS"],
# 	allow_headers=["Content-Type", "Set_Cookie", "Access-Control-Allow-Headers",
# 				 "Access-Control-Allow-Origin", "Authorization"]
# )


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")