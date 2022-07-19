import json
from datetime import datetime

from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository


class PostValidate:
    def __init__(self, repository: PostRepository, post: dict, username: str):
        self.repository = repository
        self.post = post
        self.username = username

    def validate(self):
        try:
            self.__validate_qtd_user_posts()
            self.__validate_type_post()
        except Exception as e:
            raise f"Validation error: {e}"

    def __validate_qtd_user_posts(self):
        try:
            start = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
            find = self.repository.get_by_filter(filter_by={"query": {"username": self.username,
                                                                      "date": {"$gte": start}
                                                                      },
                                                            "limit": 5})
            if len(find) >= 5:
                raise Exception(f"User {self.post['username']} exceeded limit of 5 posts a day")
        except Exception as e:
            raise Exception(f"Validation error {str(e)}")

    def __validate_type_post(self):
        if self.post['type'] == "repost":
            if self.post['original_post']['type'] == "repost":
                raise Exception(f"User {self.post['username']} Trying to repost a repost")


class ValidateUser:

    def __init__(self, user):
        self.__profile_repository = ProfileRepository()
        self.user = user
        self.username = None

    def validate_user(self):
        try:
            if not self.user:
                raise "User not informed"
            self.user = json.loads(self.user)
            data = self.__profile_repository.get_by_filter(username=self.user['username'])
            if not data:
                raise Exception("User does not exist")
            self.username = self.user['username']
            return self.user
        except Exception as e:
            raise Exception(f"Validation error: {str(e)}")
