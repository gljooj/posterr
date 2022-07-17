import os
from datetime import datetime

from pymongo import MongoClient

client = MongoClient('mongo:27017')
db = client[os.environ['DATABASE']]


class CreateTests:
    @staticmethod
    def create_user(user_collection):
        number = 0
        while number < 3:
            user_collection.insert_one({"username": f"usertest{number}", "joined_at": datetime.now()})
            number += 1

    @staticmethod
    def create_post(post_collection):
        number = 1
        post = object
        while number < 3:
            post = post_collection.insert_many([{"type": "post", "username": f"usertest{number}",
                                                 "text": "first",
                                                 "date": datetime.now()},
                                                {"type": "post", "username": f"usertest{number}",
                                                 "text": "second",
                                                 "date": datetime.now()}])
            number += 1

        return post

create = CreateTests()
print("Creating Data for Tests")
if not client['user'].find_one({"username": "usertest1"}):
    create.create_user(client['user'])
    create.create_post(client['post'])

    print("Success on Create")
print("Data Already exists")
