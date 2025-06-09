from datetime import datetime
from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Entities.CustomerEntity import CustomerEntity
from pymongo.collection import Collection
from Domain.Interfaces.ICustomerInfrastructure import ICustomerInfrastructure
from Infrastructure.MongoClientInfrastructure.Collections.CustomerCollection import CustomerCollection
from Infrastructure.MongoClientInfrastructure.Settings.MongoSetting import MongoSetting

class CustomerCommand(ICustomerInfrastructure):
    def __init__(self):
        self.db_context: MongoSetting = Services.get_instance(MongoSetting)

    async def register(self, customer: CustomerEntity) -> tuple[str, str]:
        __db: Collection = self.db_context.set_collection("Customer")
        result = await __db.insert_one(
            CustomerCollection(
                cNombre=customer.cNombre, cApellido=customer.cApellido,
                dFechaRequest= datetime.now()
            ).model_dump()
        )
        if not result.inserted_id:
            return None, "Error de registro"
        return "Registro de cliente Exitoso", None
