from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

class Schema(BaseModel):
    barcode: str = Field(...)
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example:": {
                "barcode": "078742374659",
                "name": "Great Value Vanilla Flavored Ice Cream Sandwhiches, 42 fl oz, 12 Pack"
            }
        }

class UpdateModel(BaseModel):
    barcode: Optional[str]
    name: Optional[str]

    class Config:
        schema_extra = {
            "example:": {
                "barcode": "078742374659",
                "name": "Great Value Vanilla Flavored Ice Cream Sandwhiches, 42 fl oz, 12 Pack"
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

    