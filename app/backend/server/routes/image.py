from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

image_router = APIRouter()

# Calculate the path to the 'uploaded_images' directory from the current file location
current_file_path = Path(__file__).resolve()
app_root_directory = current_file_path.parents[4]  # Adjust the number of parents based on your directory structure
uploaded_images_directory = app_root_directory / "uploaded_images"
LATEST_IMAGE_PATH = uploaded_images_directory / "image.jpeg"

@image_router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Ensure the 'uploaded_images' directory exists
    uploaded_images_directory.mkdir(parents=True, exist_ok=True)
    # Overwrite the existing file with the new one
    with open(LATEST_IMAGE_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Image uploaded successfully", "filename": LATEST_IMAGE_PATH.name}

@image_router.get("/latest")
async def get_latest_image():
    # Return the latest image if it exists
    if LATEST_IMAGE_PATH.exists():
        return FileResponse(LATEST_IMAGE_PATH)
    else:
        raise HTTPException(status_code=404, detail="No latest image found")