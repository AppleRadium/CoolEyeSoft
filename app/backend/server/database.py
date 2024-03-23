import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://raf322:Spark0702@cluster0.fhcw5oz.mongodb.net/')
db = client.cooleye
fooditems_collection = db.fooditems

def fooditems_helper(fooditem) -> dict:
    return {
        "name": fooditem["name"],
        "barcode": fooditem["barcode"]
    }

#retrieve all food items in database
async def retrieve_fooditems():
    fooditems = []
    async for fooditems in fooditems_helper.find():
        fooditems.append(fooditems_helper(fooditems))
    return fooditems

#add a new food item to the database
async def add_fooditem(fooditems_data: dict) -> dict:   
    fooditem = await fooditems_collection.insert_one(fooditems_data)
    new_fooditem = await fooditems_collection.find_one({"_barcode": fooditem.inserted_name})
    return fooditems_helper(new_fooditem)

#retrieve fooditem with matching barcode
async def retrieve_fooditem(barcode: str) -> dict:
    fooditem = await fooditems_collection.find_one({"_barcode": ObjectId(barcode)})
    if fooditem:
        return fooditems_helper(fooditem)

#update fooditem with matching barcode
async def update_fooditem(barcode: str, data: dict):
    if len(data) < 1:
        return False
    fooditem = await fooditems_collection.find_one({"_barcode": ObjectId(barcode)})
    if fooditem:
        updated_fooditem = await fooditems_collection.update_one(
            {"_barcode": ObjectId(barcode)}, {"$set": data}
        )
        if updated_fooditem:
            return True
        return False
    
#delete a food item from the database
async def delete_fooditem(barcode: str):
    fooditem = await fooditems_collection.find_one({"_barcode": ObjectId(barcode)})
    if fooditem:
        await fooditems_collection.delete_one({"_barcode":ObjectId(barcode)})
        return True
