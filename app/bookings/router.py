from datetime import date
from fastapi import APIRouter, Depends
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking
from app.exeption import RoomCanotBeBooked
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users



router = APIRouter(
	prefix='/bookings',
	tags=['Бронирование']
)


@router.get("")
async def bookings(user: Users = Depends(get_current_user)) -> list[SBooking]: #-> list[dict[str, SBooking]]:
	return await BookingsDAO.find_all(user_id=user.id)


@router.post("")
async def add_rooms(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
	booking = await BookingsDAO.add(user.id, room_id, date_from, date_to)
	if not booking:
		raise RoomCanotBeBooked