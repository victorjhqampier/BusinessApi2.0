from datetime import datetime
from Domain.Entities.CoreLoggerEntity import CoreLoggerEntity
from Domain.Interfaces.ILoggerInfraestructure import ILoggerInfraestructure
from Infrastructure.CoreDatabaseInfrastructure.Collections.LoggerCollection import LoggerCollection
from Infrastructure.CoreDatabaseInfrastructure.CoreDatabaseSetting import CoreDatabaseSetting
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

class LoggerCommand (ILoggerInfraestructure):
    __db:AsyncIOMotorCollection
    
    def __init__(self) -> None:
        db_context = CoreDatabaseSetting.get_instance()
        self._db = db_context["LoggerCollection"]
    
    async def open_log(self,cApi:str, cOperation:str, cJsonRequest:str) -> str:
        guardarMongo = await self.__db.insert_one(LoggerCollection (            
            cApi=cApi,
            cOperation= cOperation,
            dFechaRequest = datetime.now(),
            cJsonRequest = cJsonRequest
        ).dict())

        return f"{guardarMongo.inserted_id}"

    async def close_log(self,id:str, cJsonResponse:str) -> None:
        await self.__db.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"dFechaResponse": datetime.now(), "cJsonResponse": cJsonResponse, "lIsSuccess": True}}
        )

    async def close_with_error_log(self,id:str, cError:str) -> None:
        try:
            await self.__db.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"dFechaResponse": datetime.now(), "cJsonResponse": cError, "lIsSuccess": False}}
            )
        except:
            return
    
    async def get_log(self,id:str) -> CoreLoggerEntity | None:
        data = await self.__db.find_one({"_id": ObjectId(id)})

        if data == None:
            return None

        return LoggerEntity(
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