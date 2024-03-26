from fastapi import FastAPI
from .routes.fooditem import router as FoodRouter
from fastapi.middleware.cors import CORSMiddleware
#from typing import List
#from uuid import UUID, uuid4

app = FastAPI()
app.include_router(FoodRouter, tags=["Food Item"], prefix="/fooditem")
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
