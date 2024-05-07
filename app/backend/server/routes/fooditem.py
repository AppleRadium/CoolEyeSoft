from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from uuid import uuid4


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
)

food_router = APIRouter()

@food_router.post("/", response_description="Food item data added into the database")
async def add_fooditem_data(fooditem: FoodSchema = Body(...)):
    fooditem_data = jsonable_encoder(fooditem)
    fooditem_data["unique_id"] = str(uuid4())
    new_fooditem = await add_fooditem(fooditem_data)
    return ResponseModel(new_fooditem, "Food item added successfully.")
    

# Assuming retrieve_fooditems returns a list of food items
@food_router.get("/", response_model=List[FoodSchema])
async def get_fooditems():
    fooditems = await retrieve_fooditems()
    if fooditems:
        # Directly return the list
        return fooditems
    # If there are no food items, return an empty list
    return []

@food_router.get("/{id}", response_description="Food item data retrieved")
async def get_fooditem_data(id):
    fooditem = await retrieve_fooditem(id)
    if fooditem:
        return ResponseModel(fooditem, "Food item data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Food item doesn't exist.")

@food_router.put("/{id}")
async def update_fooditem_data(id: str, req: UpdateFoodModel = Body(...)):
       update_data = req.dict(exclude_unset=True)  # only include fields that were actually set
       if not update_data:
            raise HTTPException(status_code=400, detail="No data provided to update")

       updated_fooditem = await update_fooditem(id, update_data)
       if updated_fooditem:
        return ResponseModel(
            "Food item with ID: {} update is successful".format(id),
            "Food item updated successfully",
        )
       else:
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the food item data.",
        )

@food_router.delete("/{id}", response_description="Food item data deleted from the database")
async def delete_fooditem_data(id: str):
    deleted_fooditem = await delete_fooditem(id)  # Ensure this function exists in your database access layer
    if deleted_fooditem:
        return ResponseModel(
            "Food item with ID: {} removed", "Food item deleted successfully"
        )
    else:
        return ErrorResponseModel(
            "An error occurred", 404, "Food item with ID {0} doesn't exist."
        )

