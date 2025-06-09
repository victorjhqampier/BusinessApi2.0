from abc import ABC, abstractmethod

from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter


class ICustomerApplication(ABC):
    @abstractmethod
    async def save(self, idTrace:str) -> ResponseCoreAdapter:
        pass
    @abstractmethod
    async def register(self, idTrace:str) -> ResponseCoreAdapter:
        pass