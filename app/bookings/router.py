from datetime import date
from fastapi import APIRouter, Depends
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.exeption import RoomCanotBeBooked
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users



router = APIRouter(
	prefix='/bookings',
	tags=['Бронирование']
)



@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    return await BookingsDAO.find_all_with_images(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user)
):
    return await BookingsDAO.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingsDAO.delete(id=booking_id, user_id=current_user.id)
