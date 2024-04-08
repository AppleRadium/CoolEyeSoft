from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path

image_router = APIRouter()

@image_router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file to disk
    save_directory = Path("uploaded_images")
    save_directory.mkdir(exist_ok=True)
    save_path = save_directory / file.filename

    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(status_code=200, content={"message": "Image uploaded successfully", "filename": file.filename})