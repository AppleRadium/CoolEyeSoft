import motor.motor_asyncio
from bson.objectid import ObjectId

from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://raf322:Spark0702@cluster0.fhcw5oz.mongodb.net/')
db = client.cooleye
fooditems_collection = db.get_collection("fooditems")

MONGO_DETAILS = config("MONGO_DETAILS")

def fooditems_helper(fooditem) -> dict:
    return {
        "unique_id": fooditem["unique_id"],
        "Item": fooditem["Item"],
        "Count": fooditem["Count"],
        "expiration_date": fooditem["expiration_date"]
    }

#retrieve all food items in database
async def retrieve_fooditems():
    fooditems = []
    async for fooditem in fooditems_collection.find().sort("date", -1):
        fooditems.append(fooditems_helper(fooditem))
    return fooditems

#add a new food item to the database
async def add_fooditem(fooditems_data: dict) -> dict:   
    fooditem = await fooditems_collection.insert_one(fooditems_data)
    new_fooditem = await fooditems_collection.find_one({"_id": fooditem.inserted_id})
    return fooditems_helper(new_fooditem)

#retrieve food item data with matching id
async def retrieve_fooditem(id: str) -> dict:
    fooditem = await fooditems_collection.find_one({"_id": ObjectId(id)})
    if fooditem:
        return fooditems_helper(fooditem)

#update fooditem
async def update_fooditem(unique_id: str, data: dict):
    if len(data) < 1:
        return False
    fooditem = await fooditems_collection.find_one({"unique_id": unique_id})
    if fooditem:
        updated_fooditem = await fooditems_collection.update_one(
            {"unique_id": unique_id}, {"$set": data}
        )
        if updated_fooditem:
            return True
        return False
     
#delete a food item from the database
async def delete_fooditem(unique_id: str):
    # Assuming 'unique_id' is the field name in your MongoDB documents
    fooditem = await fooditems_collection.find_one({"unique_id": unique_id})
    if fooditem:
        await fooditems_collection.delete_one({"unique_id": unique_id})
        return True
    else:
        return False                               