from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Interfaces.IKafkaGettingsInfrastructure import IKafkaGettingsInfrastructure
from Infrastructure.KafkaInfrastructure.config.KafkaConsumerSetting import KafkaConsumerSetting

class KafkaGettings(IKafkaGettingsInfrastructure):
    def __init__(self):
        self.KafkaConsumer:KafkaConsumerSetting = Services.get_instance(KafkaConsumerSetting)

    async def get_consumer(self)->tuple[str,str]:
        self.KafkaConsumer.set_topics(["vcaxi-topic"])
        message,err = self.KafkaConsumer.consume_messages()
        if message is None and err is None:
            return None, None
        if err:
            return None, err
        return message, None
    
    async def consumer_commit(self, message) -> None:
        self.KafkaConsumer.commit(message["raw_message"])

