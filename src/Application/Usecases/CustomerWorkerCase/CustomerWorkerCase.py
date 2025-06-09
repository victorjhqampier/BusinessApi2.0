import json
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Interfaces.ICustomerApplication import ICustomerApplication
from Domain.Commons.CoreServices import CoreServices as Services

from Application.Interfaces.ICustomerWorkerApplication import ICustomerWorkerApplication
from Domain.Interfaces.IKafkaGettingsInfrastructure import IKafkaGettingsInfrastructure


class CustomerWorkerCase(ICustomerWorkerApplication):
    def __init__(self):
        self.__kafka_getting:IKafkaGettingsInfrastructure = Services.get_dependency(IKafkaGettingsInfrastructure)
        self.customer_case:ICustomerApplication = Services.get_dependency(ICustomerApplication)  
    async def register_user(self) -> None:
        while True:
            msg,err = await self.__kafka_getting.get_consumer()
            if msg is None and err is None:
                continue
            if err:
                print(f"error al obtener mensaje {err}")
                continue
        
            message = json.loads(msg['value'])
            if type(message) is not dict or 'idTrace' not in message:
                print(f"Error al obtener el idTrace: {message}")
                await self.__kafka_getting.consumer_commit(msg)
                continue

            print(f"este es el mensaje idTrace:[{message['idTrace']}] offset [{msg['offset']}]")
            response:ResponseCoreAdapter = await self.customer_case.register(idTrace=message['idTrace'])
            if response.status == 0:
                print(f"Error en registro {response.errors[0].message}")
                await self.__kafka_getting.consumer_commit(msg)
                continue

            await self.__kafka_getting.consumer_commit(msg)
            print(response.data)


