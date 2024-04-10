from fastapi import File, UploadFile, APIRouter, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import shutil
from pathlib import Path

image_router = APIRouter()

@image_router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Define the path relative to the current file's location
    current_file_path = Path(__file__).resolve()
    root_path = current_file_path.parent.parent.parent.parent.parent
    
    # Define the save_directory relative to the root of the app
    save_directory = root_path / "uploaded_images"
    save_directory.mkdir(exist_ok=True)
    
    save_path = save_directory / file.filename
    
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return JSONResponse(status_code=200, content={"message": "Image uploaded successfully", "filename": file.filename})

@image_router.get("/latest")
async def get_latest_image():
    # Calculate the path to the 'uploaded_images' directory from the current file location
    current_file_path = Path(__file__).resolve()
    # Adjust the traversal to correctly point to the application's root directory
    app_root_directory = current_file_path.parent.parent.parent.parent.parent
    image_directory = app_root_directory / "uploaded_images"
    
    try:
        # Example logic to find the latest image by timestamp or filename
        # This assumes images are named in a way that their names sort lexicographically
        # Adjust this logic based on how you manage uploaded images
        latest_image_path = sorted(image_directory.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="No images found")
    except Exception as e:
        # General error handling (e.g., directory doesn't exist)
        raise HTTPException(status_code=500, detail=str(e))

    return FileResponse(latest_image_path)