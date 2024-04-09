from fastapi import FastAPI
from .routes.fooditem import food_router as FoodRouter
from .routes.sensor import sensor_router as SensorRouter
from .routes.image import image_router as ImageRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(FoodRouter, tags=["Food Item"], prefix="/fooditem")
app.include_router(SensorRouter, tags=["Sensor"], prefix="/sensor")
app.include_router(ImageRouter, tags=["Image"], prefix = "/image")
origins = [
    "*",
    "https://cooleyefrontend-e4cd085ab79b.herokuapp.com/"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

