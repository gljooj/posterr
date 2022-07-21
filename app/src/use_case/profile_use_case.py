from datetime import datetime

from marshmallow import ValidationError

from src.controller import ProfileValidate
from src.core.repository.profile_repository import ProfileRepository
from src.core.schema.user_schema import UserSchema


class ProfileUseCase:
    def __init__(self):
        self.__profile_repository = ProfileRepository()

    @staticmethod
    def validate_schema(post):
        try:
            UserSchema().load(post)
        except ValidationError as err:
            raise Exception(err.messages)

    def validate_user(self, user):
        return ProfileValidate(user=user, repository=self.__profile_repository).validate_user()

    def profile_data(self, username):
        data = self.__profile_repository.get_by_filter(username=username)
        data.joined_at = str(datetime.strftime(data.joined_at, "%b %d, %y"))
        return data

    def insert_new(self, user):
        try:
            self.validate_schema(user)
            if self.__profile_repository.get_by_filter(username=user['username']):
                raise Exception(f"User '{user['username']}' already exists.")
            insert = self.__profile_repository.insert_new(user)
            return insert
        except Exception as e:
            raise Exception(f"Error to insert new. ERROR:{e}")
