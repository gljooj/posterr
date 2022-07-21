from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository
from src.use_case.post_use_case import PostUseCase
from src.use_case.profile_use_case import ProfileUseCase


class ProfileController:

    def __init__(self, user, page):
        self.user = user
        self.page = int(page)
        self.__profile_repository = ProfileRepository()
        self.__post_repository = PostRepository()
        self.use_case = ProfileUseCase()
        self.post_use_case = PostUseCase()

    def new_user(self, user):
        try:
            insert = self.use_case.insert_new(user)
            return {"body": {"message": str(insert)}}
        except Exception as e:
            return {"body": {"error": str(e)}}, 400

    def profile_page(self):
        try:
            self.user = self.use_case.validate_user(user=self.user)

            user_profile_data = self.use_case.profile_data(username=self.user.username)
            posts = self.post_use_case.profile_posts(username=self.user.username, page=self.page)
            total_posts = self.post_use_case.total_posts(username=self.user.username)

            return {"body": {"profile": dict(user_profile_data),
                             "posts": posts,
                             "total_posts": total_posts}
                    }
        except Exception as e:
            return {"body": {"error": str(e)}}, 500
