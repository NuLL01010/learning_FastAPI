from fastapi import HTTPException, status

class BookingException(HTTPException):

	status_code = 500
	detail = ""

	def __init__(self):
		super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsexception(BookingException):

	status_code=status.HTTP_409_CONFLICT
	detail="Пользователь уже существует"


class IncorrectEmailorPasswordException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Неверная почта или пароль"


class TokenExpiredexception(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Токен истёк"


class TokenAbsentException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Токен отсутствует"


class IncorrentTokenFormatException(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED
	detail="Неверный формат токена"


class UserIsNotPresentExeption(BookingException):

	status_code=status.HTTP_401_UNAUTHORIZED


class RoomCanotBeBooked(BookingException):

	status_code=status.HTTP_409_CONFLICT
	detail="Нет свободных комнат"
