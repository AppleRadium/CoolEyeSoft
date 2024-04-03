from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from ..databases.sensor import (
    
    add_sensor_data,
    retrieve_sensor_datas,
    get_latest_sensor_data,
    retrieve_sensor_data,
    dht22_collection,

)
from ..schemas.schema import (
    ErrorResponseModel,
    ResponseModel,
    SensorSchema,
    UpdateSensor,
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



"""@sensor_router.put("/{timestamp}")
async def update_sensor_data(timestamp: str, req: UpdateSensor = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_sensor = await update_sensor_data(timestamp, req)
    if updated_sensor:
        return ResponseModel(
            "Sensor data with timestamp: {} name update is successful".format(timestamp),
            "Food item name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the sensor data.",
    )"""

"""@sensor_router.delete("/{timestamp}", response_description="Food item data deleted from the database")
async def delete_sensor_data(name: str):
    deleted_fooditem = await delete_fooditem(name)
    if deleted_fooditem:
        return ResponseModel(
            "Food item with name: {} removed".format(name), "Food item deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Food item with name {0} doesn't exist".format(id)
    )"""