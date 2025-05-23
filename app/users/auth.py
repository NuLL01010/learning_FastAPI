

from passlib.context import CryptContext
from jwt import encode
from app.config import settings

from app.users.dao import UsersDAO
from datetime import datetime, timedelta



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
	return pwd_context.hash(password)


def verify_password(plain_passwowrd, hashed_password) -> bool:
	return pwd_context.verify(plain_passwowrd, hashed_password)


def create_access_token(data: dict) -> str:
	to_encode = data.copy()
	expire = datetime.utcnow() + timedelta(minutes=30)
	to_encode.update({'exp': expire})
	encoded_jwt = encode(
		to_encode, settings.SECRET_KEY, settings.ALGORITHM
	)
	return encoded_jwt


async def authenticate_user(email: str, password: str):
	user = await UsersDAO.find_one_or_none(email=email)
	if user and verify_password(password, user.hashed_password):
		return user
