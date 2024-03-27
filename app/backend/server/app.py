from fastapi import FastAPI, WebSocket
from .routes.routes import food_router, sensor_router
from fastapi.middleware.cors import CORSMiddleware
#from uuid import UUID, uuid4
from typing import List


app = FastAPI()
app.include_router(food_router, tags=["Food Item"], prefix="/fooditem")
app.include_router(sensor_router, tags=["Sensor"], prefix="/sensor")
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

