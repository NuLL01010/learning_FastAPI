from pydantic import BaseModel, EmailStr


class SUsersAuth(BaseModel):
	email: EmailStr
	password: str