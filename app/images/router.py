from fastapi import APIRouter, UploadFile
import shutil

from app.tasks.tasks import upload_image

router = APIRouter(
	prefix="/images",
	tags=["Картинки"]
)


@router.post("hotels")
async def add_hotel_photo(name: int, file: UploadFile):
	im_path = f"app/static/images/{name}.webp"
	with open(im_path, "wb+") as file_object:
		shutil.copyfileobj(file.file, file_object)
	upload_image.delay(im_path)