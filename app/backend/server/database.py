import motor.motor_asyncio
from bson.objectid import ObjectId

from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://raf322:Spark0702@cluster0.fhcw5oz.mongodb.net/')
db = client.cooleye
fooditems_collection = db.get_collection("fooditems")
dht22_collection = db.get_collection("tempandhumid")

MONGO_DETAILS = config("MONGO_DETAILS")

def fooditems_helper(fooditem) -> dict:
    return {
        "id": str(fooditem["_id"]),
        "name": fooditem["name"],
    }

def sensor_data_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "timestamp": data["timestamp"],
    }

#retrieve all food items in database
async def retrieve_fooditems():
    fooditems = []
    async for fooditem in fooditems_collection.find().sort("date", -1):
        fooditems.append(fooditems_helper(fooditem))
    return fooditems
#retrieve all DHT22 data in database
async def retrieve_sensor_datas():
    sensor_data = []
    async for data in dht22_collection.find().sort("timestamp", -1):
        sensor_data.append(sensor_data_helper(data))
    return sensor_data
#add a new food item to the database
async def add_fooditem(fooditems_data: dict) -> dict:   
    fooditem = await fooditems_collection.insert_one(fooditems_data)
    new_fooditem = await fooditems_collection.find_one({"_id": fooditem.inserted_id})
    return fooditems_helper(new_fooditem)
#add a new sensor data to the database
async def add_sensor_data(sensor_data: dict) -> dict:   
    sensor = await dht22_collection.insert_one(sensor_data)
    new_sensor = await dht22_collection.find_one({"_id": sensor.inserted_id})
    return fooditems_helper(new_sensor)
#retrieve fooditem with matching barcode
async def retrieve_fooditem(id: str) -> dict:
    fooditem = await fooditems_collection.find_one({"_id": ObjectId(id)})
    if fooditem:
        return fooditems_helper(fooditem)
#retrieve sensor data with matching id
async def retrieve_sensor_data(id: str) -> dict:
    sensor = await dht22_collection.find_one({"_id": ObjectId(id)})
    if sensor:
        return fooditems_helper(sensor)
#update fooditem
async def update_fooditem(id: str, data: dict):
    if len(data) < 1:
        return False
    fooditem = await fooditems_collection.find_one({"_id": ObjectId(id)})
    if fooditem:
        updated_fooditem = await fooditems_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_fooditem:
            return True
        return False
    
#update sensor  
async def update_sensor(id: str, data: dict):
    if len(data) < 1:
        return False
    sensor = await dht22_collection.find_one({"_id": ObjectId(id)})
    if sensor:
        updated_sensor = await dht22_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_sensor:
            return True
        return False
    
#delete a food item from the database
async def delete_fooditem(id: str):
    fooditem = await fooditems_collection.find_one({"_id": ObjectId(id)})
    if fooditem:
        await fooditems_collection.delete_one({"_id":ObjectId(id)})
        return True
