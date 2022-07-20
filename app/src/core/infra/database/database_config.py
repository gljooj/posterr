import os

from pymongo import MongoClient


class DataBaseConfig:
    client = MongoClient(host=os.environ['DATABASE'],
                         port=27017,
                         username=os.environ['ROOT_USERNAME'],
                         password=os.environ['ROOT_PASSWORD'],
                         authSource="admin")
    db = client.posterr
