import smtplib
from pydantic import EmailStr
from app.config import settings
from app.tasks.celery import celery
from pathlib import Path
from PIL import Image

from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def upload_image(
		paht: int
):
	im_path = Path(paht)
	im = Image.open(im_path)
	im_resized_300_200 = im.resize((300, 200))
	im_resized_1000_500 = im.resize((1000, 500))
	im_resized_300_200.save(f"app/static/images/im_resized_300_200{im_path.name}")
	im_resized_1000_500.save(f"app/static/images/im_resized_1000_500{im_path.name}")


@celery.task
def send_booking_confirmation_email(
	booking: dict,
	email_to: EmailStr
):
	msg_content = create_booking_confirmation_template(booking, email_to)

	with smtplib.SMTP_SSL(host=settings.SMTP_HOST, port=settings.SMTP_PORT) as server:
		server.login(settings.SMTP_USER, settings.SMTP_PASS)
		server.send_message(msg_content)
