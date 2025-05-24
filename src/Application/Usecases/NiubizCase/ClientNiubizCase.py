from Application.Interfaces.IClientNiubizCaseApplication import IClientNiubizCaseApplication
from Domain.Entities.Client.ClientResponseEntity import ClientResponseEntity
from Domain.Interfaces.IClientInfrastructure import IClientInfrastructure
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Domain.Commons.CoreServices import CoreServices as Services

class ClientNiubizCase(IClientNiubizCaseApplication):
    def __init__(self):
        self.__client_repo:IClientInfrastructure = Services.get_dependency(IClientInfrastructure)
        self.__easy_response= EasyResponseCoreHelper()
    
    async def get_client(self, CustomerCardIdentifier:int, CustomerCardNumber:str)->ResponseCoreAdapter:
        # do some validations
        result:ClientResponseEntity = await self.__client_repo.get_client(CustomerCardIdentifier,CustomerCardNumber)
        
        if result.data is not None:
            return self.__easy_response.EasySuccessRespond(result.data)
        
        if result.errors is not None:
            return self.__easy_response.EasyListErrorRespond(result.errors)
        
        return self.__easy_response.EasyEmptyRespond(result.errors)