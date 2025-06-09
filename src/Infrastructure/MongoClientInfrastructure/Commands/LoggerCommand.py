from datetime import datetime
from bson import ObjectId
from pymongo.collection import Collection
from Domain.Commons.CoreServices import CoreServices as Services

from Domain.Entities.CoreLoggerEntity import CoreLoggerEntity
from Domain.Interfaces.ILoggerInfraestructure import ILoggerInfraestructure
from Infrastructure.MongoClientInfrastructure.Collections.LoggerCollection import LoggerCollection
from Infrastructure.MongoClientInfrastructure.Settings.MongoSetting import MongoSetting

class LoggerCommand (ILoggerInfraestructure):
    def __init__(self) -> None:
        self.db_context:MongoSetting = Services.get_instance(MongoSetting)
    
    async def open_log(self,cApi:str, cOperation:str, cJsonRequest:str) -> str:
        __db:Collection = self.db_context.set_collection('LoggerCollection')
        guardarMongo = await __db.insert_one(LoggerCollection (            
            cApi=cApi,
            cOperation= cOperation,
            dFechaRequest = datetime.now(),
            cJsonRequest = cJsonRequest
        ).model_dump())

        return f"{guardarMongo.inserted_id}"

    async def close_log(self,id:str, cJsonResponse:str) -> None:
        __db:Collection = self.db_context.set_collection('LoggerCollection')
        await __db.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"dFechaResponse": datetime.now(), "cJsonResponse": cJsonResponse, "lIsSuccess": True}}
        )

    async def close_with_error_log(self,id:str, cError:str) -> None:
        __db:Collection = self.db_context.set_collection('LoggerCollection')
        await __db.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"dFechaResponse": datetime.now(), "cJsonResponse": cError, "lIsSuccess": False}}
        )

    
    async def get_log(self,id:str) -> CoreLoggerEntity | None:
        __db:Collection = self.db_context.set_collection('LoggerCollection')
        data = await __db.find_one({"_id": ObjectId(id)})

        if data is None:
            return None

        return CoreLoggerEntity(
            idLogger=f'{data["_id"]}',
            idPadre=data["idPadre"],
            cApi=data["cApi"],
            cOperation=data["cOperation"],
            dFechaRequest=data["dFechaRequest"],
            cJsonRequest=data["cJsonRequest"],
            dFechaResponse=data["dFechaResponse"],
            cJsonResponse=data["cJsonResponse"],
            lIsSuccess=data["lIsSuccess"]
        )

