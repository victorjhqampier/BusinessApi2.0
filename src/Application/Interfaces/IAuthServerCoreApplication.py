from abc import ABC, abstractmethod

class IAuthServerCoreApplication(ABC):
    @abstractmethod
    async def get_cognito_token(self)->str:
        pass