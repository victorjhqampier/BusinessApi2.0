from abc import ABC, abstractmethod


class ICustomerWorkerApplication(ABC):
    @abstractmethod
    async def register_user(self) -> None:
        pass
