

from Domain.Commons.Template.KafkaConsumerTemplate import KafkaConsumerTemplate


class KafkaConsumerSetting(KafkaConsumerTemplate):
    def set_topics(self, topics: list[str]) -> None:
        if self.topics != topics:
            self.topics = topics
            self.subscribe()
       
