from typing import Any
from confluent_kafka import Consumer
from abc import ABC


class KafkaConsumerTemplate(ABC):
    def __init__(self, bootstrap_servers: str, group_id: str, security_config: dict[str,Any] = None):
        config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False  
        }

        if security_config:
            config.update(security_config)

        self.consumer = Consumer(config)
        self.topics = []

    def set_topics(self, topics: list[str]) -> None:
        self.topics = topics

    def subscribe(self):
        if not self.topics:
            raise ValueError("Debe establecer al menos un tópico antes de suscribirse.")
        self.consumer.subscribe(self.topics)

    def consume_messages(self, timeout: float = 1.0)->tuple[str,str]:
        msg = self.consumer.poll(timeout)
        if msg is None:
            return None, None
        if msg.error():
            return None, msg.error()

        message_data = {
            "topic": msg.topic(),
            "partition": msg.partition(),
            "offset": msg.offset(),
            "key": msg.key().decode('utf-8') if msg.key() else None,
            "value": msg.value().decode('utf-8') if msg.value() else None,
            "raw_message": msg  
        }

        return message_data, None

    def commit(self, msg):
        self.consumer.commit(msg)

    def close(self):
        self.consumer.close()
