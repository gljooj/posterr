from datetime import datetime

from src.core.repository.post_repository import PostRepository


class PostValidate:
    def __init__(self, repository: PostRepository, post):
        self.repository = repository
        self.post = post

    def validate(self):
        try:
            self.__validate_qtd_user_posts()
            self.__validate_type_post()
        except Exception as e:
            raise f"Validation error: {e}"

    def __validate_qtd_user_posts(self):
        start = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
        find = self.repository.get_by_filter(filter_by={"query": {"username": self.post['username'],
                                                                  "date": {"$gte": start}
                                                                  },
                                                        "limit": 5})
        if len(find) >= 5:
            raise Exception(f"User {self.post['username']} exceeded limit of 5 posts a day")

    def __validate_type_post(self):
        if self.post['type'] == "repost":
            if self.post['original_post']['type'] == "repost":
                raise Exception(f"User {self.post['username']} Trying to repost a repost")
