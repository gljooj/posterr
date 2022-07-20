from datetime import datetime

from src.core.infra.database.database_config import DataBaseConfig


class CreateTests(DataBaseConfig):
    __db = DataBaseConfig.db

    def setup(self):
        print("Creating Data for Tests")

        if not self.__db.user.find_one({"username": "usertest1"}):
            self.create_user(self.__db.user)
            self.create_post(self.__db.post)
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
        number_user = 1
        days_post = 1
        post = object
        while number_user < 3:
            while days_post < 3:
                post = post_collection.insert_many([{"type": "post", "username": f"usertest{number_user}",
                                                     "text": "this is my post",
                                                     "created_date": datetime(2022, 7, 18 + days_post, 4, 55, 5)},

                                                    {"type": "repost", "username": f"usertest{number_user}",
                                                     "original_post": {"type": "post",
                                                                       "username": f"usertest{number_user}",
                                                                       "text": "this is my post"},
                                                     "created_date": datetime(2022, 7, 18 + days_post, 5, 55, 5)},

                                                    {"type": "quote-post", "username": f"usertest{number_user}",
                                                     "text": "This is my quote-post",
                                                     "original_post": {"type": "post",
                                                                       "username": f"usertest{number_user}",
                                                                       "text": "this is my post",
                                                                       "created_date": datetime(2022, 7, 18, 4, 55, 5)},
                                                     "created_date": datetime(2022, 7, 18 + days_post, 6, 55, 5)},

                                                    {"type": "quote-post", "username": f"usertest{number_user}",
                                                     "text": "This is my quote-post",
                                                     "original_post": {"type": "repost",
                                                                       "username": f"usertest{number_user}",
                                                                       "original_post": {"type": "post",
                                                                                         "username": f"usertest{number_user}",
                                                                                         "text": "this is my post"},
                                                                       "created_date": datetime(2022, 7, 18, 5, 55, 5)},
                                                     "created_date": datetime(2022, 7, 18 + days_post, 7, 55, 5)},

                                                    {"type": "repost", "username": f"usertest{number_user}",
                                                     "original_post": {"type": "quote-post",
                                                                       "username": f"usertest{number_user}",
                                                                       "text": "This is my quote-post",
                                                                       "original_post": {"type": "post",
                                                                                         "username": f"usertest{number_user}",
                                                                                         "text": "this is my post",
                                                                                         "created_date": datetime(2022,
                                                                                                                  7, 18,
                                                                                                                  4, 55,
                                                                                                                  5)},
                                                                       "created_date": datetime(2022, 7, 18, 6, 55, 5)},
                                                     "created_date": datetime(2022, 7, 18 + days_post, 8, 55, 5)},

                                                    ])
                days_post += 1
            number_user += 1

        return post


print(CreateTests().setup())
