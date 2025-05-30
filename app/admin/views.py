from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users



class UsersAdmin(ModelView, model=Users):
	column_list = [Users.id, Users.email]

	column_details_exclude_list = [Users.hashed_password]

	can_delete = False

	name = "Пользователь"
	name_plural = "Пользователи"
	icon = "fa-solid fa-user"
	category = "Users"


class BookingsAdmin(ModelView, model=Bookings):
	column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user] + [Bookings.room]

	name = "Бронь"
	name_plural = "Брони"
	category = "Bookings"


class RoomsAdmin(ModelView, model=Rooms):
	column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel]

	name = "Комната"
	name_plural = "Комнаты"
	category = "Rooms"


class HotelsAdmin(ModelView, model=Hotels):
	column_list = [c.name for c in Hotels.__table__.c] + [Hotels.room]

	name = "Отель"
	name_plural = "Отели"
	category = "Hotels"