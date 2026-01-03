from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.CoreApplicationSetting import CoreApplicationSetting
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Presentation.BusinessApi.Controllers.ExampleController import ExampleController
from Presentation.EventListener.FromExternal.KafkaConsumerSetting import KafkaConsumerSetting
from Presentation.EventListener.FromMemory.MemoryListenerSetting import MemoryListenerSetting
from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager
import asyncio

# ********************************************************************************************************          
# * Copyright © 2026 Arify Labs - All rights reserved.   
# * 
# * Info                  : Integrator for SaaS.
# *
# * By                    : Victor Jhampier Caxi Maquera
# * Email/Mobile/Phone    : victorjhampier@gmail.com | 968991*14
# *
# * Creation date         : 01/01/2026
# * 
# **********************************************************************************************************

# ----- Start Coroutine -----
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Add Memory listener
    await MemoryListenerSetting.add_services()

    # Add Application layer
    CoreApplicationSetting()

    # Add Kafka consumer
    # my_consumers = KafkaConsumerSetting()
    # await my_consumers.add_services()
    
    try:
        yield
    finally:
        pass
        # await my_consumers.stop_services()

app = FastAPI(docs_url="/docs/openapi", redoc_url="/docs/reopenapi", lifespan=lifespan)
app.title = "Arify Backend Business Layer"
app.version = "1.0"

@app.get("/", response_model=ResponseCoreAdapter)
def default():
    EasyResponse = EasyResponseCoreHelper()
    return EasyResponse.EasySuccessRespond( {"Info":"Arify Labs All rights reserved" })

@app.get("/health")
async def health():
    return {"status": "ok"}

# Add Example APIs
app.include_router(ExampleController, prefix="/example-service-b/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")