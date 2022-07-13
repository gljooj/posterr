from datetime import datetime
import pymongo


class Profile:

    def __init__(self, username):
        self.username = username

    def payload(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        db = myclient['posterr']

        collection = db['user'].find_one({"username": self.username}, {"_id": False})

        date = collection.get("joined_at")
        format_date = datetime.fromisoformat(date)
        print(format_date)
        return date