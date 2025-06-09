from pymongo import AsyncMongoClient
from pymongo.collection import Collection
from abc import ABC


class MongoConnectionTemplate(ABC):
    def __init__(self, db_type: str, user: str, password: str, server: str, db_name: str):
        self.client = AsyncMongoClient(f"{db_type}://{user}:{password}@{server}")
        self.db_name = db_name
        self.db = self.client[self.db_name]
        self.collection = None

    def set_collection(self, collection_name: str) -> None:
        if self.collection != collection_name:
            self.collection = collection_name

    def get_connection(self) -> Collection:
        if not self.collection:
            raise ValueError("Debes de establecer al menos una collecion.")
        return self.db[self.collection]
