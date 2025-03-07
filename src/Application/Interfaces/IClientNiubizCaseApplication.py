from abc import ABC, abstractmethod

from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter

class IClientNiubizCaseApplication(ABC):
    @abstractmethod
    async def get_client(self, CustomerCardIdentifier:int, CustomerCardNumber:str)->ResponseCoreAdapter:
        pass