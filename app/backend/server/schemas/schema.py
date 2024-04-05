from datetime import datetime
from typing import Annotated, Any, Callable, Optional
from bson import ObjectId

from pydantic import BaseModel, ConfigDict, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic.functional_validators import BeforeValidator
class _ObjectIdPydanticAnnotation:
    # Based on https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types.

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(input_value: str) -> ObjectId:
            return ObjectId(input_value)

        return core_schema.union_schema(
            [
                # check if it's an instance first before doing any further work
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ],
            serialization=core_schema.to_string_ser_schema(),
        )
    

PydanticObjectId = Annotated[
    ObjectId, _ObjectIdPydanticAnnotation
]

#PydanticObjectId = Annotated[str, BeforeValidator(str)]
class FoodSchema(BaseModel):

    #id: Optional[PydanticObjectId] = Field(alias="_id", default = None)
    id: Optional[PydanticObjectId] = Field(alias="_id")
    Item: str = Field(...)
    Count: int = Field(..., description = "count of food item")
    model_config = ConfigDict (
        arbitrary_types_allowed = True,
        json_encoders = {ObjectId: str},
        populate_by_name=True,
        allow_population_by_alias = True)

   

class UpdateFoodModel(BaseModel):
    
    
    #id: Optional[PydanticObjectId] = Field(alias="_id", default = None)
    id: Optional[PydanticObjectId] = Field(alias="_id")
    Item: Optional[str]
    Count: Optional[int] = Field(None, description = "updated count of food item")
    model_config = ConfigDict(
        allow_population_by_alias = True
    )
    


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

    