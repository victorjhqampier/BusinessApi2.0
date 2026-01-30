from abc import ABC, abstractmethod

from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter

class IClientNiubizCasePort(ABC):
    @abstractmethod
    async def get_client(self, CustomerCardIdentifier:int, CustomerCardNumber:str)->ResponseCoreAdapter:
        pass