import asyncio

from Presentation.Queues.Queries.ExamExecuteFromKafkaQuery import ExamExecuteFromKafkaQuery
from Presentation.Queues.Services.KafkaConsumerService import KafkaConsumerService
from Presentation.Queues.Collections.ExampleTopicCollection import ExampleTopicCollection

class KafkaConsumerSetting():

    def __init__(self) -> None:
        self.__consumers = [
            KafkaConsumerService[ExampleTopicCollection]()
                .with_topic("vcaxi-topic")
                .with_group_id("Combined Lag")
                .with_bootstrap_servers("10.5.81.14:9092")
                .with_handler(ExamExecuteFromKafkaQuery)
        ]
    
    async def add_services(self) -> "KafkaConsumerSetting":
        await asyncio.gather(*(consumer.start() for consumer in self.__consumers))
    
    async def stop_services(self) -> None:
        await asyncio.gather(*(consumer.stop() for consumer in self.__consumers))