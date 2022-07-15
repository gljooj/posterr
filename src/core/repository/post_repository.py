import pymongo
from datetime import datetime

from src.core.repository.abstract_repository import AbstractRepository
from src.core.schemas.post import PostSchema


class PostRepository(AbstractRepository):

    def get_by_filter_paginate(self, filter_by):
        # page - 1 to start from last data
        limit = filter_by["limit"]
        skip = (filter_by['page'] - 1) * limit

        data = self.db['post'].find(
            filter_by["query"], {"_id": False}).sort('date', pymongo.DESCENDING).skip(skip).limit(filter_by["limit"])
        items = []
        for item in data:
            items.append(item)
        return items

    def get_by_filter(self, filter_by):
        data = self.db['post'].find(filter_by["query"], {"_id": False})
        items = []
        for item in data:
            items.append(item)
        return items

    def insert_new(self, post: dict):
        post.update({"date": datetime.today().strftime('%Y-%m-%d %H:%M:%S')})
        insert = self.db['post'].insert_one(post)
        return insert.inserted_id
