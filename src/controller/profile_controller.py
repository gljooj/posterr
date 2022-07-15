from datetime import datetime

from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository


class ProfileController:

    def __init__(self, username, page):
        self.username = username
        self.page = int(page)
        self.profile_repository = ProfileRepository()
        self.post_repository = PostRepository()

    @property
    def __profile_data(self):
        data = self.profile_repository.get_by_filter(username=self.username)
        data['joined_at'] = str(datetime.strftime(data.get("joined_at"), "%b %d, %y"))
        return data

    def __profile_post(self):
        print(self.page)
        data = self.post_repository.get_by_filter_paginate(filter_by={"query": {"username": self.username},
                                                                      "page": self.page,
                                                                      "limit": 5})
        print(data)
        return data

    def profile_page(self):
        print(self.page)
        posts = self.__profile_post()
        return {"body": {"profile": self.__profile_data,
                         "posts": posts}
                }
