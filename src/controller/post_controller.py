from pprint import pprint

from marshmallow import ValidationError

from src.core.repository import PostValidate
from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository
from src.core.schemas.post import PostSchema


class PostController:
    __post_repository = PostRepository()
    __profile_repository = ProfileRepository()

    @staticmethod
    def validate_schema(post):
        try:
            PostSchema().load(post)
        except ValidationError as err:
            pprint(err.messages)
            raise Exception(err.messages)

    def validate_profile(self, username):
        data = self.__profile_repository.get_by_filter(username=username)
        if not data:
            raise Exception("User does not exist")

    def validate_post(self, post):
        # check if users did 5 posts
        self.validate_schema(post)
        PostValidate(self.__post_repository, post).validate()

    def new_post(self, post):
        try:
            print("post")
            self.validate_profile(post['username'])
            self.validate_post(post)
            insert = self.__post_repository.insert_new(post)
            return {"body": {"message": str(insert)}}

        except Exception as e:
            return {"body": {"error": str(e)}}, 400
