from fastapi.testclient import TestClient
from pymongo import MongoClient
from bson import ObjectId
import pytest
from app import app


client = TestClient(app)
mongo_client = MongoClient('mongodb+srv://raf322:Spark0702@cluster0.fhcw5oz.mongodb.net/')
db = mongo_client['fooditems']


def test_get_fooditems_no_params():
    response = client.get("/fooditem")
    assert response.status_code == 200
