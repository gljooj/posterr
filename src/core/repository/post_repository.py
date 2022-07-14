import pymongo

from src.core.repository.abstract_repository import AbstractRepository


class PostRepository(AbstractRepository):
    def get_by_filter(self, filter_by):
        # page - 1 to start from last data
        skip = (filter_by['page'] - 1) * 5
        limit = filter_by["limit"]
        del filter_by['page']
        del filter_by['limit']

        data = self.db['post'].find(filter_by, {"_id": False}).sort('date', pymongo.DESCENDING).skip(skip).limit(limit)
        items = []
        for item in data:
            items.append(item)
        return items

    def bulk_upsert_new(self, bulk: []):
        pass
