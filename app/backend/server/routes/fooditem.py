from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..databases.fooditem import (
    add_fooditem,
    delete_fooditem,
    retrieve_fooditem,
    retrieve_fooditems,
    update_fooditem,
   

)
from ..schemas.schema import (
    ErrorResponseModel,
    ResponseModel,
    FoodSchema,
    UpdateFoodModel,
    SensorSchema,
    UpdateSensor,
)

food_router = APIRouter()
sensor_router = APIRouter()

@food_router.post("/", response_description="Food item data added into the database")
async def add_fooditem_data(fooditem: FoodSchema = Body(...)):
    fooditem = jsonable_encoder(fooditem)
    new_fooditem = await add_fooditem(fooditem)
    return ResponseModel(new_fooditem, "Food item added successfully.")
    

@food_router.get("/", response_description="Food items retrieved")
async def get_fooditems():
    fooditems = await retrieve_fooditems()
    if fooditems:
        return ResponseModel(fooditems, "Food items data retrieved successfully")
    return ResponseModel(fooditems, "Empty list returned")


@food_router.get("/{name}", response_description="Food item data retrieved")
async def get_fooditem_data(name):
    fooditem = await retrieve_fooditem(name)
    if fooditem:
        return ResponseModel(fooditem, "Food item data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Food item doesn't exist.")

@food_router.put("/{name}")
async def update_fooditem_data(name: str, req: UpdateFoodModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_fooditem = await update_fooditem(name, req)
    if updated_fooditem:
        return ResponseModel(
            "Food item with name: {} name update is successful".format(name),
            "Food item name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the food item data.",
    )

@food_router.delete("/{name}", response_description="Food item data deleted from the database")
async def delete_fooditem_data(name: str):
    deleted_fooditem = await delete_fooditem(name)
    if deleted_fooditem:
        return ResponseModel(
            "Food item with name: {} removed".format(name), "Food item deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Food item with name {0} doesn't exist".format(id)
    )

@sensor_router.post("/", response_description="Sensor data added into the database")
async def add_sensor_data(sensor: SensorSchema = Body(...)):
    sensor = jsonable_encoder(sensor)
    new_sensor = await add_fooditem(sensor)
    return ResponseModel(new_sensor, "Data added successfully.")
    

@sensor_router.get("/", response_description="Sensor data list retrieved")
async def get_sensor_data_list():
    sensordatas = await retrieve_sensor_datas()
    if sensordatas:
        return ResponseModel(sensordatas, "Sensor data list retrieved successfully")
    return ResponseModel(sensordatas, "Empty list returned")


@sensor_router.get("/{timestamp}", response_description="Sensor data retrieved")
async def get_sensor_data(timestamp):
    sensor = await retrieve_sensor_data(timestamp)
    if sensor:
        return ResponseModel(sensor, "Sensor data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Food item doesn't exist.")

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