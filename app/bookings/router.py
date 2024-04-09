from datetime import date
from fastapi import APIRouter, BackgroundTasks, Depends
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.exeption import RoomCanotBeBooked
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

from pydantic.type_adapter import TypeAdapter
from pydantic import parse_obj_as
from app.config import settings
from app.tasks.tasks import send_booking_confirmation_email

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
    backgroundTasks: BackgroundTasks,
    user: Users = Depends(get_current_user)

):
    booking = await BookingsDAO.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)

    # booking_dict = TypeAdapter.validate_python(SBooking, booking, strict=False).dict()
    # booking_dict = parse_obj_as(SBooking, booking).dict()

    # send_booking_confirmation_email.delay() не работает, ебал гугл и форматы с которыми работает celery

    backgroundTasks.add_task(send_booking_confirmation_email(booking, settings.SMTP_USER))

    return booking



@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingsDAO.delete(id=booking_id, user_id=current_user.id)
