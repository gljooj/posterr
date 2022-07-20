from datetime import datetime

from marshmallow import ValidationError

from src.controller import ProfileValidate
from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository
from src.core.schemas.user_schema import UserSchema


class ProfileController:

    def __init__(self, user, page=1):
        self.user = user
        self.page = int(page)
        self.__profile_repository = ProfileRepository()
        self.__post_repository = PostRepository()

    @staticmethod
    def validate_schema(post):
        try:
            UserSchema().load(post)
        except ValidationError as err:
            raise Exception(err.messages)

    @property
    def __profile_data(self):
        data = self.__profile_repository.get_by_filter(username=self.user['username'])
        data['joined_at'] = str(datetime.strftime(data.get("joined_at"), "%b %d, %y"))
        return data

    def __profile_posts(self):
        data = self.__post_repository.get_by_filter_paginate(filter_by={"query": {"username": self.user['username']},
                                                                        "page": self.page,
                                                                        "limit": 5})
        return data

    def __total_posts(self):
        data = self.__post_repository.get_by_filter(filter_by={"query": {"username": self.user['username']}})
        return data["count"]

    def new_user(self, user):
        try:
            self.validate_schema(user)
            if self.__profile_repository.get_by_filter(username=user['username']):
                raise Exception(f"User '{user['username']}' already exists.")
            insert = self.__profile_repository.insert_new(user)
            return {"body": {"message": str(insert)}}
        except Exception as e:
            return {"body": {"error": str(e)}}, 400

    def profile_page(self):
        try:
            self.user = ProfileValidate(self.user).validate_user()
            user = self.__profile_data
            posts = self.__profile_posts()
            total_posts = self.__total_posts()
            return {"body": {"profile": user,
                             "posts": posts,
                             "total_posts": total_posts}
                    }
        except Exception as e:
            return {"body": {"error": str(e)}}, 500
