from datetime import datetime

from src.core.repository.abstract_repository import AbstractRepository
from src.core.schema import UserObject


class ProfileRepository(AbstractRepository):

    def get_by_filter_paginate(self, data):
        pass

    def get_by_filter(self, username) -> UserObject:
        data = self.db.user.find_one({"username": username}, {"_id": False})
        return UserObject(username=username, joined_at=data['joined_at'])

    def insert_new(self, user):
        user['joined_at'] = datetime.now()
        insert = self.db.user.insert_one(user)
        return insert.inserted_id
