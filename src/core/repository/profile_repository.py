from src.core.repository.abstract_repository import AbstractRepository


class ProfileRepository(AbstractRepository):

    def get_by_filter(self, username):
        data = self.db['user'].find_one({"username": username}, {"_id": False})
        print(data)
        return data

    def bulk_upsert_new(self, bulk):
        pass
