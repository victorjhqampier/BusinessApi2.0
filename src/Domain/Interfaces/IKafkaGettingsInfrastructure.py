from abc import ABC, abstractmethod


class IKafkaGettingsInfrastructure(ABC):
    @abstractmethod
    async def get_consumer(self) -> tuple[str, str]:
        pass

    @abstractmethod
    async def consumer_commit(self, message) -> None:
        pass




