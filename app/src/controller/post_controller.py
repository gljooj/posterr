from src.use_case.post_use_case import PostUseCase


class PostController:
    def __init__(self):
        self.post_use_case = PostUseCase()

    def new_post(self, post: dict, user: str):
        try:
            insert = self.post_use_case.insert_new(post=post, user=user)

            return {"body": {"message": str(insert)}}
        except Exception as e:
            return {"body": {"error": str(e)}}, 400
