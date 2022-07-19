from pymongo import MongoClient


class DataBaseConfig:
    client = MongoClient(host='mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource="admin")
    db = client.posterr
