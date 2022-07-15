from datetime import datetime

from marshmallow import ValidationError, pprint

from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository
from src.core.schemas.user_schema import UserSchema


class ProfileController:

    def __init__(self, username, page):
        self.username = username
        self.page = int(page)
        self.profile_repository = ProfileRepository()
        self.post_repository = PostRepository()

    @staticmethod
    def validate_schema(post):
        try:
            UserSchema().load(post)
        except ValidationError as err:
            pprint(err.messages)
            raise Exception(err.messages)

    @property
    def __profile_data(self):
        data = self.profile_repository.get_by_filter(username=self.username)
        data['joined_at'] = str(datetime.strftime(data.get("joined_at"), "%b %d, %y"))
        return data

    def __profile_posts(self):
        print(self.page)
        data = self.post_repository.get_by_filter_paginate(filter_by={"query": {"username": self.username},
                                                                      "page": self.page,
                                                                      "limit": 5})
        print(data)
        return data

    def new_user(self, user):
        try:
            self.validate_schema(user)
            if self.profile_repository.get_by_filter(username=user['username']):
                raise Exception(f"User '{user['username']}' already exists.")
            insert = self.profile_repository.insert_new(user)
            return {"body": {"message": str(insert)}}
        except Exception as e:
            return {"body": {"error": str(e)}}, 400

    def profile_page(self):
        try:
            print(self.page)
            posts = self.__profile_posts()
            return {"body": {"profile": self.__profile_data,
                             "posts": posts}
                    }
        except Exception as e:
            return {"body": {"error": str(e)}}, 500

