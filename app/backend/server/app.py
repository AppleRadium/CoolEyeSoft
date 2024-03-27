from fastapi import FastAPI, WebSocket
from .routes.fooditem import food_router as FoodRouter
from .routes.sensor import sensor_router as SensorRouter
from fastapi.middleware.cors import CORSMiddleware
#from uuid import UUID, uuid4
from typing import List


app = FastAPI()
app.include_router(FoodRouter, tags=["Food Item"], prefix="/fooditem")
app.include_router(SensorRouter, tags=["Sensor"], prefix="/sensor")
origins = [
    "*"
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

