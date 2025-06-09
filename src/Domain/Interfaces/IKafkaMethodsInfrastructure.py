from abc import ABC, abstractmethod

from Domain.Entities.KafkaEntity import KafkaEntity
class IKafkaMethodsInfrastructure(ABC):
    @abstractmethod
    async def send_message(self, key: str, value: KafkaEntity) -> tuple[str, str]:
        pass
