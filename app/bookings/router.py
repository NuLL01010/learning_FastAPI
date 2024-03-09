from fastapi import APIRouter
from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking



router = APIRouter(
	prefix='/booking',
	tags=['Бронирование']
)


@router.get("")
async def bookings() -> list[SBooking]:#-> list[dict[str, SBooking]]:
	return await BookingsDAO.find_all()