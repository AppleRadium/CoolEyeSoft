from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from ..databases.sensor import (
    
    add_sensor_data,
    retrieve_sensor_datas,
    get_latest_sensor_data,

)
from ..schemas.schema import (

    ResponseModel,
    SensorSchema,
)

sensor_router = APIRouter()


@sensor_router.post("/", response_description="Sensor data added into the database")
async def add_sensor(sensor: SensorSchema = Body(...)):
    sensor = jsonable_encoder(sensor)
    new_sensor = await add_sensor_data(sensor)
    return ResponseModel(new_sensor, "Data added successfully.")
    

@sensor_router.get("/", response_description="Sensor data list retrieved")
async def get_sensor_data_list():
    sensordatas = await retrieve_sensor_datas()
    if sensordatas:
        return ResponseModel(sensordatas, "Sensor data list retrieved successfully")
    return ResponseModel(sensordatas, "Empty list returned")

@sensor_router.get("/latest")
async def fetch_latest_sensor_data():
    latest_data = await get_latest_sensor_data()
    if not latest_data:
        raise HTTPException(status_code=404, detail="No sensor data found")
    return {"temperature": latest_data["temperature"], "humidity": latest_data["humidity"], "timestamp": latest_data["timestamp"]}
