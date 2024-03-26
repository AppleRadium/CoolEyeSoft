from fastapi import FastAPI, WebSocket
from .routes.fooditem import router as FoodRouter
from fastapi.middleware.cors import CORSMiddleware
#from uuid import UUID, uuid4
from typing import List

connected_clients: List[WebSocket] = []

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

@app.websocket("/ws")
async def sensor_data(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Here you would parse the incoming data and possibly save it to MongoDB
            for client in connected_clients:
                await client.send_text(data)  # Echo data to all connected clients
    except Exception as e:
        print(e)
    finally:
        connected_clients.remove(websocket)