from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

image_router = APIRouter()

# Calculate the save_directory based on the current file's location
current_file_path = Path(__file__).resolve()
root_path = current_file_path.parent.parent.parent.parent.parent
save_directory = root_path / "uploaded_images"
save_directory.mkdir(exist_ok=True)  # Ensure the directory exists

@image_router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_location = save_directory / file.filename
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": "Image uploaded successfully", "filename": file.filename}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred while uploading the image.")

@image_router.get("/latest")
async def get_latest_image():
    try:
        # Find the most recently modified file
        latest_image_path = max(save_directory.iterdir(), key=lambda x: x.stat().st_mtime, default=None)
        if latest_image_path:
            return FileResponse(latest_image_path)
        else:
            raise HTTPException(status_code=404, detail="No images found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred while retrieving the image.")
