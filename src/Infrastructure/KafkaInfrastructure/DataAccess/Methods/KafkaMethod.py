from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Entities.KafkaEntity import KafkaEntity
from Domain.Interfaces.IKafkaMethodsInfrastructure import IKafkaMethodsInfrastructure
from Infrastructure.KafkaInfrastructure.config.KafkaProducerSetting import KafkaProducerSetting

class KafkaMethod(IKafkaMethodsInfrastructure):

    def __init__(self):
        self.producer: KafkaProducerSetting = Services.get_instance(KafkaProducerSetting)

    async def send_message(self, key: str, value: KafkaEntity) -> tuple[str, str]:
        self.producer.set_topic("vcaxi-topic")
        self.producer.produce_message(key=key, value=value.model_dump())
        try:
            self.producer.flush()
            return "envio correcto", None
        except Exception as e:
            return None, f"erro de envio {e}"
