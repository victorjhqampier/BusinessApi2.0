import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

class CoreDatabaseSetting:    
    _instance = None
    def __new__(cls, *args, **kwargs):

        load_dotenv()
        
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.client = AsyncIOMotorClient(f"{os.getenv('MONGO_DB_TYPE')}://{os.getenv('MONGO_DB_USER')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_SERVER')}")
            cls._instance.db_name = f"{os.getenv('MONGO_DB_NAME')}"
        return cls._instance

    @classmethod
    def get_instance(cls):        
        instance = cls()
        db = instance.client[instance.db_name]
        return db