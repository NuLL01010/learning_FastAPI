from pydantic import EmailStr
from email.message import EmailMessage

from app.config import settings


def create_booking_confirmation_template(
		booking: dict,
		email_to: EmailStr
):
	email = EmailMessage()

	email["Subject"] = "Подтверждение бронирования"
	email["From"] = settings.SMTP_USER
	email["To"] = settings.SMTP_USER

	email.set_content(
		f"""
			<h1>Подтвердите бронирование</h1>
			Вы забронировали отель с ... по ...
		""",
		subtype="html"
	)

	return email