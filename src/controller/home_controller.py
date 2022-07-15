from datetime import datetime

from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository


class HomeController:
    def __init__(self, user, page):
        self.user = user
        self.page = int(page)
        self.profile_repository = ProfileRepository()
        self.post_repository = PostRepository()

    @property
    def __profile_data(self):
        data = self.profile_repository.get_by_filter(username=self.user['username'])
        data['joined_at'] = str(datetime.strftime(data.get("joined_at"), "%b %d, %y"))
        return data

    def __profile_post(self):
        data = self.post_repository.get_by_filter_paginate(filter_by={"query": {}, "page": self.page,
                                                                      "limit": 10})
        print(data)
        return data

    def home_page(self):
        posts = self.__profile_post()
        return {"body": {"profile": self.__profile_data,
                         "posts": posts}
                }
