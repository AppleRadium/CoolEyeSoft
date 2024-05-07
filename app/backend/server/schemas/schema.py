from datetime import datetime, timedelta
from typing import Annotated, Optional
from uuid import UUID
from pydantic import BaseModel, Field, validator
from pydantic.functional_validators import BeforeValidator

PydanticObjectId = Annotated[str, BeforeValidator(str)]

expiration_duration = {
    #duration = number of days
    "apple": {
        "duration": 28,
        "aliases": ["apple","apples", "Apple", "Apples"]
    },
    "banana": {
        "duration": 5,
        "aliases": ["banana","bananas", "Banana", "Bananas"]
    },
    "cabbage" :{
        "duration": 56,
        "aliases": ["cabbage","cabbages", "Cabbage", "Cabbages"]
    },
    "asparagus": {
        "duration": 4,
        "aliases": ["asparagus","asparaguses", "Asparagus", "Asparaguses"]
    },
    "potato":{
        "duration": 56,
        "aliases": ["potato","potatoe", "Potato", "Potatoes", "Potatoe"]
    } ,
    "mango": {
        "duration": 14,
        "aliases": ["mango","mangoes", "Mango", "Mangoes"]
    },
    "bell pepper":{
        "duration": 7,
        "aliases": ["bell pepper","bell peppers", "Bell Pepper", "Bell Peppers"]
    } ,
    "orange":{
        "duration": 28,
        "aliases": ["orange","oranges", "Orange", "Oranges"]
    },
    "watermelon": {
        "duration": 14,
        "aliases": ["watermelon","watermelons", "Watermelon", "Watermelons"]
    },
    "strawberry": {
        "duration": 7,
        "aliases": ["strawberry","strawberries", "Strawberry", "Strawberries"]
    },
    "pear": {
        "duration": 4,
        "aliases": ["pear","pears", "Pear", "Pears"]
    },
    "carrot": {
        "duration": 21,
        "aliases": ["carrot","carrots", "Carrot", "Carrots"]
    },
    "pomegranate":{
        "duration": 30,
        "aliases": ["pomegranate","pomegranates", "Pomegranate", "Pomegranates"]
    } ,
    "peach": {
        "duration": 4,
        "aliases": ["peach","peaches", "Peach", "Peaches"]
    },
    "cucumber": {
        "duration": 7,
        "aliases": ["cucumber","cucumbers", "Cucumber", "Cucumbers"]
    },
    "pineapple": {
        "duration": 7,
        "aliases": ["pineapple","pineapples", "Pineapple", "Pineapples"]
    },
    "lemon": {
        "duration": 14,
        "aliases": ["lemon","lemons", "Lemon", "Lemons"]
    },
    "tomato":{
        "duration": 5,
        "aliases": ["tomato","tomatoes", "Tomato", "Tomatoes"]
    } ,
    "grape bunch": {
        "duration": 14,
        "aliases": ["grape bunch","grapes", "Grapes", "grape", "Grape", "Grape bunch", "Grape Bunch"]
    },
    "zucchini": {
        "duration": 7,
        "aliases": ["zucchini","Zucchini", "zucchinis", "Zucchinis"]
    },
    "broccoli": {
        "duration": 4,
        "aliases": ["broccoli", "Broccoli", "broccolis", "Broccolis"]
    },
    "mushroom": {
        "duration": 5,
        "aliases": ["mushroom","mushrooms", "Mushroom", "Mushrooms"]
    },
    "cantaloupe": {
        "duration": 21,
        "aliases": ["cantaloupe", "Cantaloupe", "cantaloupes", "Cantaloupes"]
    }
}

def find_expiration_duration(item_name):
    normalized_name = item_name.lower().strip()
    for key, value in expiration_duration.items():
        if normalized_name in value['aliases']:
            return value['duration']
    return None

class FoodSchema(BaseModel):

    unique_id: Optional[str] = Field(None, description="The unique identifier for the food item")
    Item: str = Field(...)
    Count: int = Field(..., description="count of food item")
    expiration_date: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {UUID: lambda v: str(v)}
        populate_by_name = True
        allow_population_by_alias = True
    
    @validator('expiration_date', pre=True, always=True)
    def set_expiration_date(cls, v, values):
        if 'Item' in values:
            duration_days = find_expiration_duration(values['Item'])
            if duration_days is not None:
                added_date = values.get('added_date', datetime.now())
                return added_date + timedelta(days=duration_days)
        return v

   

class UpdateFoodModel(BaseModel):
    
    Item: Optional[str]
    Count: Optional[int] = Field(None, description = "updated count of food item")
    expiration_date: Optional[datetime] = Field(default=None, example="2024-01-01T00:00:00.000Z")
    
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

    