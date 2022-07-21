from marshmallow import ValidationError

from src.controller import PostValidate
from src.core.repository.post_repository import PostRepository
from src.core.schema.post_schema import PostSchema
from src.use_case.profile_use_case import ProfileUseCase


class PostUseCase:
    def __init__(self):
        self.__post_repository = PostRepository()
        self.profile_use_case = ProfileUseCase()

    @staticmethod
    def validate_schema(post):
        try:
            PostSchema().load(post)
        except ValidationError as err:
            raise Exception(err.messages)

    def validate_post(self, post, username):
        # check if users already did 5 posts
        return PostValidate(self.__post_repository, post, username).validate()

    def profile_posts(self, username, page):
        data = self.__post_repository.get_by_filter_paginate(filter_by={"query": {"username": username},
                                                                        "page": page,
                                                                        "limit": 5})
        return data

    def total_posts(self, username):
        data = self.__post_repository.get_by_filter(filter_by={"query": {"username": username}})
        return data["count"]

    def get_by_filter_paginate(self, query):
        data = self.__post_repository.get_by_filter_paginate(filter_by=query)
        return data

    def insert_new(self, post, user):
        try:
            user = self.profile_use_case.validate_user(user)
            post["username"] = user.username

            self.validate_post(post, user.username)

            insert = self.__post_repository.insert_new(post)
            return {"body": {"message": "Post Created",
                             "post_id": str(insert)
                             }
                    }
        except Exception as e:
            raise Exception(f"Error to insert new. ERROR: {e}")
