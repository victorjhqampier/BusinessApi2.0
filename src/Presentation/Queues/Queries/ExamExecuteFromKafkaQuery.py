from Presentation.Queues.Collections.ExampleTopicCollection import ExampleTopicCollection
import time

class ExamExecuteFromKafkaQuery:
    def __init__(self, event: ExampleTopicCollection) -> None:
        self.__event = event
        self.handle_vcaxi()

    def handle_vcaxi(self) -> None:        
        #time.sleep(3)
        print(f"Arify: [handler-1] order {str(self.__event)}")
    
    @classmethod
    async def create(cls, event: ExampleTopicCollection):
        instance = cls(event)
        await instance.handle_vcaxi()
        return instance