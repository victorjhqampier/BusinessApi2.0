from abc import ABC, abstractmethod

from Domain.Entities.CustomerEntity import CustomerEntity


class ICustomerInfrastructure(ABC):
    @abstractmethod
    async def register(self, customer: CustomerEntity) -> tuple[str, str]:
        pass
