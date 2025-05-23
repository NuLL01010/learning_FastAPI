from fastapi import APIRouter, Depends, Response
from app.exeption import IncorrectEmailorPasswordException, UserAlreadyExistsexception
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

from app.users.schemas import SUsersAuth

router = APIRouter(
	prefix="/auth",
	tags=["auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUsersAuth):
	existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
	if existing_user:
		raise UserAlreadyExistsexception()
	hashed_password = get_password_hash(user_data.password)
	await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUsersAuth):
	user = await authenticate_user(email=user_data.email, password=user_data.password)
	if not user:
		raise IncorrectEmailorPasswordException()
	access_token = create_access_token({"sub": str(user.id)})
	response.set_cookie("Booking_accesss_token", access_token, httponly=True)
	return access_token


@router.post("/logout")
async def loguot_user(response: Response):
	response.delete_cookie("Booking_accesss_token")


@router.post("/me")
async def get_me_current_user(user: Users = Depends(get_current_user)):
	return user