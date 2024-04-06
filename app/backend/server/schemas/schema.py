from datetime import datetime
from typing import Annotated, Any, Callable, Optional
from bson import ObjectId
from uuid import uuid4, UUID
from pydantic import BaseModel, ConfigDict, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic.functional_validators import BeforeValidator


PydanticObjectId = Annotated[str, BeforeValidator(str)]
class FoodSchema(BaseModel):

    unique_id: Optional[str] = Field(None, description="The unique identifier for the food item")
    Item: str = Field(...)
    Count: int = Field(..., description="count of food item")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {UUID: lambda v: str(v)}
        populate_by_name = True
        allow_population_by_alias = True

   

class UpdateFoodModel(BaseModel):
    
    Item: Optional[str]
    Count: Optional[int] = Field(None, description = "updated count of food item")
    
    class Config: 
        arbitrary_types_allowed = True
        json_encoders = {UUID: lambda v: str(v)}
        populate_by_name = True
        allow_population_by_alias = True
    


class SensorSchema(BaseModel):
    temperature: float = Field(..., example=24.5)
    humidity: float = Field(..., example=40.2)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "temperature": 24.5,
                "humidity": 40.2,
                "timestamp": "2023-03-18T12:00:00"
            }
        }

class UpdateSensor(BaseModel):
    temperature: Optional[float]
    humidity: Optional[float]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "temperature": 24.5,
                "humidity": 40.2,
                "timestamp": "2023-03-18T12:00:00"
            }
        }

def ResponseModel(data, message):
    return{
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return{"error": error, "code": code, "message": message}

    