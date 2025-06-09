from contextlib import asynccontextmanager
import asyncio
from Application.Interfaces.ICustomerWorkerApplication import ICustomerWorkerApplication
from Domain.Commons.CoreServices import CoreServices as Services

import threading
from fastapi import FastAPI

from Infrastructure.KafkaInfrastructure.config.KafkaConsumerSetting import KafkaConsumerSetting

@asynccontextmanager
async def lifespan(app: FastAPI):
    kafka: ICustomerWorkerApplication = Services.get_dependency(ICustomerWorkerApplication)
    print("Iniciando el consumidor Kafka.")
    hilo = threading.Thread(target=lambda:asyncio.run(kafka.register_user(), debug=False),daemon=False,name='hilo_Kafka_consumer')
    hilo.start()
    yield
        
    KafkaConsumer = Services.get_instance(KafkaConsumerSetting) 
    KafkaConsumer.close()
    print("Cerrando el consumidor Kafka.")
