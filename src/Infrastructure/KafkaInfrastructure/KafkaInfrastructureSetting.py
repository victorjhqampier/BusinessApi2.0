from Domain.Commons.CoreServices import CoreServices as Services
# from Domain.Interfaces.IKafkaGettingsInfrastructure import IKafkaGettingsInfrastructure
from Domain.Interfaces.IKafkaGettingsInfrastructure import IKafkaGettingsInfrastructure
from Domain.Interfaces.IKafkaMethodsInfrastructure import IKafkaMethodsInfrastructure
# from Infrastructure.KafkaInfrastructure.DataAccess.Gettings.KafkaGettings import KafkaGettings
from Infrastructure.KafkaInfrastructure.DataAccess.Gettings.KafkaGettings import KafkaGettings
from Infrastructure.KafkaInfrastructure.DataAccess.Methods.KafkaMethod import KafkaMethod
from Infrastructure.KafkaInfrastructure.config.KafkaConsumerSetting import KafkaConsumerSetting
from Infrastructure.KafkaInfrastructure.config.KafkaProducerSetting import KafkaProducerSetting 

class KafkaInfrastructureSetting:
    @classmethod
    def add_services(self) -> None:

        Services.add_singleton_instance(
            KafkaProducerSetting(
                bootstrap_servers="10.5.81.14:9092",
                client_id="obesito",
            )
        )
        Services.add_singleton_instance(
            KafkaConsumerSetting(
                bootstrap_servers="10.5.81.14:9092",
                group_id="obesito"
            )
        )

        Services.add_singleton_dependency(IKafkaMethodsInfrastructure, KafkaMethod)
        Services.add_singleton_dependency(IKafkaGettingsInfrastructure, KafkaGettings)
