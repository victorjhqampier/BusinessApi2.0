from pymongo.collection import Collection

from Domain.Commons.Template.MongoConnectionTemplate import MongoConnectionTemplate


class MongoSetting(MongoConnectionTemplate):
    def set_collection(self, collection_name: str) -> Collection:
        if self.collection != collection_name:
            self.collection = collection_name
        return self.get_connection()
