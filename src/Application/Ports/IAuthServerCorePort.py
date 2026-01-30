from abc import ABC, abstractmethod

class IAuthServerCorePort(ABC):
    @abstractmethod
    async def get_cognito_token(self)->str:
        pass