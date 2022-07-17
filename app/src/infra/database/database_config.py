import pymongo
from pymongo import MongoClient


class DataBaseConfig:
    __client = pymongo.MongoClient("mongodb://localhost:27017/")
    MongoClient('mongo:27017')

    db = __client['posterr']

