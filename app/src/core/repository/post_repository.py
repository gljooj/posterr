import pymongo
from datetime import datetime

from src.core.repository.abstract_repository import AbstractRepository


class PostRepository(AbstractRepository):

    def get_by_filter_paginate(self, filter_by):
        try:
            # page - 1 to start from last data
            limit = filter_by["limit"]
            skip = (filter_by["page"] - 1) * limit
            data = self.db.post.find(
                filter_by["query"], {"_id": False}).sort('created_date', pymongo.DESCENDING).\
                skip(skip).limit(filter_by["limit"])
            items = []
            for item in data:
                item['created_date'] = datetime.isoformat(item['created_date'])
                items.append(item)
            return items
        except Exception as e:
            raise e

    def get_by_filter(self, filter_by):

        if 'limit' in filter_by:
            data = self.db.post.find(filter_by["query"], {"_id": False}).limit(filter_by['limit'])
        else:
            data = self.db.post.find(filter_by["query"], {"_id": False})

        items = {"data": []}
        for item in data:
            items["data"].append(item)
        items.update({"count": len(items["data"])})
        return items

    def insert_new(self, post: dict):
        post.update({"created_date": datetime.today()})
        insert = self.db.post.insert_one(post)
        return insert.inserted_id
