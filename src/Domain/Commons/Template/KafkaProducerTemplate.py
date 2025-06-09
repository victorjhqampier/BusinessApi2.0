import json
from typing import Any
from confluent_kafka import Producer, KafkaError
from abc import ABC


class KafkaProducerTemplate(ABC):
    def __init__(self, bootstrap_servers: str, client_id: str, security_config: dict[str, Any] = None) -> None:

        config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': client_id
        }

        if security_config:
            config.update(security_config)

        self.producer = Producer(config)
        self.topic = None

    def set_topic(self, topic_name: str) -> None:
        self.topic = topic_name

    def delivery_report(self, err: KafkaError | None, msg) -> None:
        if err is not None:
            print(f"[Kafka] Error entregando mensaje: {err}")
        else:
            print(
                f"[Kafka] topic {msg.topic()} "
                f"[part {msg.partition()}] offset {msg.offset()}"
            )
            
    def produce_message(self, value: dict[str, Any], key: str | None = None):
        if not self.topic:
            raise ValueError("Debe establecer un topico antes de enviar mensajes.")
        self.producer.produce(
            topic=self.topic,
            key=key,
            value=json.dumps(value),
            callback=self.delivery_report
        )
        self.producer.poll(0)  

    def flush(self):
        self.producer.flush()


