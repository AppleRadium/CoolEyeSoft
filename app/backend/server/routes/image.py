from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path

image_router = APIRouter()

@image_router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Path to the current file (image.py)
    current_file_path = Path(__file__).resolve()

    # Navigate up three levels to the server directory
    server_directory = current_file_path.parent.parent.parent

    # Define the save_directory path
    save_directory = server_directory / "uploaded_images"
    save_directory.mkdir(exist_ok=True)
    save_path = save_directory / file.filename

    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(status_code=200, content={"message": "Image uploaded successfully", "filename": file.filename})

'''@image_router.get("/latest-image")
async def get_latest_image():
    image_directory = Path("uploaded_images")
    # Example logic to find the latest image by timestamp or filename
    # This assumes images are named in a way that their names sort lexicographically
    # Adjust this logic based on how you manage uploaded images
    latest_image_path = sorted(image_directory.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)[0]
    return FileResponse(latest_image_path)'''