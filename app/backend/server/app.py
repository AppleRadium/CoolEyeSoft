from fastapi import FastAPI, HTTPException, WebSocket
from server.routes.fooditem import router as FoodRouter
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

"""@app.websocket("/environmental-data")
async def environmental_data(websocket: WebSocket):
    await websocket.accept()
    while True:
        update = await receive_environmental_update()
        if update:
            await websocket.send_json({
                "temperature": update['temperature'],
                "humidity": update['humidity'],
                "timestamp": update['timestamp']
            })
        await asyncio.sleep(10)  # Wait for a bit before checking for new data"""