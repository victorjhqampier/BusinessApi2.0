import json
from Application.Adpaters.GlobalErrorCoreAdapter import GlobalErrorCoreAdapter
from Application.Interfaces.ILoggerCoreApplication import ILoggerCoreApplication
from Domain.Commons.CoreServices import CoreServices as Services
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Interfaces.ICustomerApplication import ICustomerApplication
from Domain.Entities.CoreLoggerEntity import CoreLoggerEntity
from Domain.Entities.CustomerEntity import CustomerEntity
from Domain.Entities.KafkaEntity import KafkaEntity
from Domain.Interfaces.ICustomerInfrastructure import ICustomerInfrastructure
from Domain.Interfaces.IKafkaMethodsInfrastructure import IKafkaMethodsInfrastructure


class CustomerCase(ICustomerApplication):
    def __init__(self):
        self.__KafkaMethod:IKafkaMethodsInfrastructure = Services.get_dependency(IKafkaMethodsInfrastructure)
        self.__MongoClient:ILoggerCoreApplication = Services.get_dependency(ILoggerCoreApplication)
        self.__user:ICustomerInfrastructure = Services.get_dependency(ICustomerInfrastructure)

    async def save(self, idTrace:str) -> ResponseCoreAdapter:
        _ , err = await self.__KafkaMethod.send_message(key="Obesito",value=KafkaEntity(idTrace=idTrace,nIntentos=0))
        err:str
        if err:
            return ResponseCoreAdapter(status=0,errors=[GlobalErrorCoreAdapter(
                code=0,
                message=err,
                field=f"Error {err}"
            )])
        return ResponseCoreAdapter(status=1,data={"Message":"Cliente registrado exitosamente."})
    
    async def register(self, idTrace:str) -> ResponseCoreAdapter:
        result = await self.__MongoClient.get_log(idTrace)
        if not result:
            return ResponseCoreAdapter(status=0,errors=[GlobalErrorCoreAdapter(
                code=0,
                message='No hay registro en mongo',
                field=f"Error {'No hay registro en mongo'}"
            )])
        result:CoreLoggerEntity
        user_temp = json.loads(result.cJsonRequest)
        meesage, err_registro = await self.__user.register(CustomerEntity(cApellido=user_temp.get('apellido'),cNombre=user_temp.get('nombre')))
        if err_registro:
            return ResponseCoreAdapter(status=0,errors=[GlobalErrorCoreAdapter(
                code=0,
                message=err_registro,
                field=f"Error {err_registro}"
            )])
        return ResponseCoreAdapter(status=1,data={"Message":meesage})

