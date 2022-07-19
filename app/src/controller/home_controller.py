from datetime import datetime

from src.controller import ValidateUser
from src.core.repository.post_repository import PostRepository
from src.core.repository.profile_repository import ProfileRepository


class HomeController:
    def __init__(self, user, page, post_from, start_at, end_at):
        """filter_posts = All/ Only Mine"""
        self.user = user
        self.page = int(page)
        self.post_from = post_from
        self.start_at = start_at
        self.end_at = end_at
        self.__profile_repository = ProfileRepository()
        self.__post_repository = PostRepository()

    def define_query(self):
        if self.post_from not in ['all', 'only-mine']:
            raise Exception('Filter must be all or only-mine')
        if self.post_from == 'all':
            return {}
        return self.user

    def define_date_query(self):
        query = None
        if self.end_at:
            query = {"created_date": {"$lt": datetime.strptime(self.end_at, '%Y-%m-%d %H:%M:%S')}}

            if self.start_at:
                return {"created_date": {"$lt": datetime.strptime(self.end_at, '%Y-%m-%d %H:%M:%S'),
                                         "$gte": datetime.strptime(self.start_at, '%Y-%m-%d %H:%M:%S')}}

        if self.start_at:
            query = {"created_date": {"$gte": datetime.strptime(self.start_at, '%Y-%m-%d %H:%M:%S')}}

        return query

    @property
    def __profile_data(self):
        data = self.__profile_repository.get_by_filter(username=self.user['username'])
        data['joined_at'] = str(datetime.strftime(data.get("joined_at"), "%b %d, %y"))
        return data

    def __posts(self):
        query = self.define_query()
        date = self.define_date_query()
        if date:
            query.update(date)

        data = self.__post_repository.get_by_filter_paginate(filter_by={"query": query, "page": self.page,
                                                                        "limit": 10})
        return data

    def home_page(self):
        try:
            self.user = ValidateUser(self.user)
            posts = self.__posts()
            return {"body": {"profile": self.__profile_data,
                             "posts": posts}
                    }
        except Exception as e:
            return {"body": {"error": str(e)}}, 500
