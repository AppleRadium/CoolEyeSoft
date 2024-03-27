import motor.motor_asyncio
from bson.objectid import ObjectId

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
    async for data in dht22_collection.find().sort("timestamp", -1):
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
    
