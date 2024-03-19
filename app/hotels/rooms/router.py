from typing import List, Optional
from datetime import date, timedelta, datetime


from fastapi import APIRouter, Depends, Query
from app.bookings.dao import BookingsDAO
from app.exeption import RoomCanotBeBooked
from app.hotels.dao import HotelDAO
from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomInfo
from app.hotels.schemas import SHotel
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
	prefix='/rooms',
	tags=['Rooms']
)

@router.post("")
async def add_rooms(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
	booking = await BookingsDAO.add(user.id, room_id, date_from, date_to)
	if not booking:
		raise RoomCanotBeBooked


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SRoomInfo]:
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotel]:
    return await HotelDAO.find_one_or_none(id=hotel_id)