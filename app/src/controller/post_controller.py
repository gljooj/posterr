from marshmallow import ValidationError

from src.controller import PostValidate, ProfileValidate
from src.core.schemas.post_schema import PostSchema
from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository


class PostController:
    __post_repository = PostRepository()
    __profile_repository = ProfileRepository()

    def __init__(self, user):
        self.username = None
        self.user = user

    @staticmethod
    def validate_schema(post):
        try:
            PostSchema().load(post)
        except ValidationError as err:
            raise Exception(err.messages)

    def validate_user(self):
        self.user = ProfileValidate(self.user).validate_user()

    def validate_post(self, post):
        # check if users already did 5 posts
        self.validate_schema(post)
        post_validate = PostValidate(self.__post_repository, post, self.username)
        post_validate.validate()

    def new_post(self, post):
        try:
            self.validate_user()
            post["username"] = self.user['username']
            self.validate_post(post)
            insert = self.__post_repository.insert_new(post)
            return {"body": {"message": str(insert)}}

        except Exception as e:
            return {"body": {"error": str(e)}}, 400
