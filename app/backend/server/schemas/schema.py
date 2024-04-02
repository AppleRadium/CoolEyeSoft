from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class FoodSchema(BaseModel):
   
    Item: str = Field(...)
    Count: int = Field(..., description = "count of food item")

    class Config:
        schema_extra = {
            "example:": {
                "Item": "Great Value Vanilla Flavored Ice Cream Sandwhiches, 42 fl oz, 12 Pack",
                "Count": 5
            }
        }

class UpdateFoodModel(BaseModel):
    
    Item: Optional[str]
    Count: Optional[int] = Field(None, description = "updated count of food item")

    class Config:
        schema_extra = {
            "example:": {
                "Item": "Great Value Vanilla Flavored Ice Cream Sandwhiches, 42 fl oz, 12 Pack",
                "Count": 5
            }
        }


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

    