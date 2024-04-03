import motor.motor_asyncio
from bson.objectid import ObjectId
from pymongo import DESCENDING
from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://raf322:Spark0702@cluster0.fhcw5oz.mongodb.net/')
db = client.cooleye
dht22_collection = db.get_collection("tempandhumid")

MONGO_DETAILS = config("MONGO_DETAILS")


def sensor_data_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "timestamp": data["timestamp"],
    }

async def retrieve_sensor_datas():
    sensor_data = []
    async for data in dht22_collection.find().sort("date", -1):
        sensor_data.append(sensor_data_helper(data))
    return sensor_data

async def add_sensor_data(sensor_data: dict) -> dict:   
    sensor = await dht22_collection.insert_one(sensor_data)
    new_sensor = await dht22_collection.find_one({"_id": sensor.inserted_id})
    return sensor_data_helper(new_sensor)

async def retrieve_sensor_data(id: str) -> dict:
    sensor = await dht22_collection.find_one({"_id": ObjectId(id)})
    if sensor:
        return sensor_data_helper(sensor)
    
async def get_latest_sensor_data():
    # Assuming `sensor_collection` is an instance of AsyncIOMotorCollection
    latest_data_cursor = dht22_collection.find().sort("timestamp", -1).limit(1)
    latest_data_list = await latest_data_cursor.to_list(length=1)
    if latest_data_list:
        # Return the most recent entry.
        return latest_data_list[0]
    else:
        # Return None if no data is found.
        return None
