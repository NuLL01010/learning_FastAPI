from app.tasks.celery import celery
from pathlib import Path
from PIL import Image


@celery.task()
def upload_image(
		paht: int
):
	im_path = Path(paht)
	im = Image.open(im_path)
	im_resized_300_200 = im.resize((300, 200))
	im_resized_1000_500 = im.resize((1000, 500))
	im_resized_300_200.save(f"app/static/images/im_resized_300_200{im_path.name}")
	im_resized_1000_500.save(f"app/static/images/im_resized_1000_500{im_path.name}")