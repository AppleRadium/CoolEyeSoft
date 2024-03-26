from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_fooditem,
    delete_fooditem,
    retrieve_fooditem,
    retrieve_fooditems,
    update_fooditem,
)
from ..schemas.fooditem import (
    ErrorResponseModel,
    ResponseModel,
    FoodSchema,
    UpdateFoodModel,
)

router = APIRouter()

@router.post("/", response_description="Food item data added into the database")
async def add_fooditem_data(fooditem: FoodSchema = Body(...)):
    fooditem = jsonable_encoder(fooditem)
    new_fooditem = await add_fooditem(fooditem)
    return ResponseModel(new_fooditem, "Food item added successfully.")
    

@router.get("/", response_description="Food items retrieved")
async def get_fooditems():
    fooditems = await retrieve_fooditems()
    if fooditems:
        return ResponseModel(fooditems, "Food items data retrieved successfully")
    return ResponseModel(fooditems, "Empty list returned")


@router.get("/{name}", response_description="Food item data retrieved")
async def get_fooditem_data(name):
    fooditem = await retrieve_fooditem(name)
    if fooditem:
        return ResponseModel(fooditem, "Food item data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Food item doesn't exist.")

@router.put("/{name}")
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

@router.delete("/{name}", response_description="Food item data deleted from the database")
async def delete_fooditem_data(name: str):
    deleted_fooditem = await delete_fooditem(name)
    if deleted_fooditem:
        return ResponseModel(
            "Food item with name: {} removed".format(name), "Food item deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Food item with name {0} doesn't exist".format(id)
    )