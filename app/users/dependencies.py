from datetime import datetime
from fastapi import Depends, Request
# from jose import JWTError
from jwt import decode
from jwt import PyJWTError
from app.config import settings
from app.exeption import IncorrentTokenFormatException, TokenAbsentException, TokenExpiredexception, UserIsNotPresentExeption
from app.users.dao import UsersDAO



def get_token(request: Request):
	token = request.cookies.get("Booking_accesss_token")
	if not token:
		raise TokenAbsentException()
	return token


async def get_current_user(token: str = Depends(get_token)):
	try:
		payload = decode(
			token, settings.SECRET_KEY, settings.ALGORITHM
		)
	except PyJWTError:
		raise IncorrentTokenFormatException()

	expire: str = payload.get("exp")
	if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
		raise TokenExpiredexception()
	user_id: str = payload.get("sub")
	if not user_id:
		raise UserIsNotPresentExeption()
	user = await UsersDAO.find_by_id((int(user_id)))
	if not user:
		raise UserIsNotPresentExeption()

	return user
