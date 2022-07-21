from datetime import datetime
from src.use_case.post_use_case import PostUseCase
from src.use_case.profile_use_case import ProfileUseCase


class HomeController:
    def __init__(self, user, page, post_from, start_at, end_at):
        """filter_posts = All/ Only Mine"""
        self.profile_use_case = ProfileUseCase()
        self.post_use_case = PostUseCase()
        self.user = user
        self.page = int(page)
        self.post_from = post_from
        self.start_at = start_at
        self.end_at = end_at

    def define_filter(self):
        if self.post_from not in ['all', 'only-mine']:
            raise Exception('Filter must be all or only-mine')
        if self.post_from == 'all':
            return {}
        return {"username": self.user.username}

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

    def __posts(self):
        query = {"query": self.define_filter(), "page": self.page, "limit": 10}
        date = self.define_date_query()
        if date:
            query["query"].update(date)
        data = self.post_use_case.get_by_filter_paginate(query=query)
        return data

    def home_page(self):
        try:
            self.user = self.profile_use_case.validate_user(self.user)
            posts = self.__posts()
            profile = self.profile_use_case.profile_data(self.user.username)
            return {"body": {"profile": profile,
                             "posts": posts}
                    }
        except Exception as e:
            return {"body": {"error": str(e)}}, 500
