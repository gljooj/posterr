from datetime import datetime

from src.core.infra.database.database_config import DataBaseConfig

db = DataBaseConfig.db


class CreateTests(DataBaseConfig):
    def setup(self):
        print("Creating Data for Tests")

        if not db.user.find_one({"username": "usertest1"}):
            self.create_user(db.user)
            self.create_post(db.post)
            print("Success on Create data for tests")
            return "Success on Create data for tests"

        print("Data Already Created data for tests")
        return "Data Already Created data for tests"

    @staticmethod
    def create_user(user_collection):
        number = 0
        while number < 3:
            user_collection.insert_one({"username": f"usertest{number}",
                                        "joined_at": datetime(2022, 7, 17, 4 + number, 55, 5)})
            number += 1

    @staticmethod
    def create_post(post_collection):
        number = 1
        post = object
        while number < 3:
            post = post_collection.insert_many([{"type": "post", "username": f"usertest{number}",
                                                 "text": "first",
                                                 "created_date": datetime.now()},
                                                {"type": "post", "username": f"usertest{number}",
                                                 "text": "second",
                                                 "created_date": datetime(2022, 7, 18, 4 + number, 55, 5)}])
            number += 1

        return post
