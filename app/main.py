from typing import Optional

from fastapi import Depends, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from redis import asyncio as aioredis
from sqladmin import Admin, ModelView

from app.admin.auth import authentication_backend
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.bookings.router import router as router_bookings
from app.database import engine
from app.hotels.rooms.router import router as router_rooms
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.pages.router import router as router_pages
from app.users.router import router as router_users

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




admin = Admin(app, engine, authentication_backend=authentication_backend)



admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(HotelsAdmin)