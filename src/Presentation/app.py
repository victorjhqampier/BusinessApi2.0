from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.CoreApplicationSetting import CoreApplicationSetting
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Presentation.Controllers.CustomerController import CustomerController
from Presentation.Controllers.ExampleController import ExampleController
from fastapi import FastAPI
import uvicorn

from WorkerServices.CustomerWorker import lifespan

# ********************************************************************************************************          
# * Copyright © 2025 Arify Labs - All rights reserved.   
# * 
# * Info                  : Integrator for SaaS.
# *
# * By                    : Victor Jhampier Caxi Maquera
# * Email/Mobile/Phone    : victorjhampier@gmail.com | 968991*14
# *
# * Creation date         : 20/10/2024
# * 
# **********************************************************************************************************

EasyResponse = EasyResponseCoreHelper()
#Add Core Services
CoreApplicationSetting()

app = FastAPI(docs_url="/", redoc_url="/docs/reopenapi",lifespan=lifespan)
app.title = "Arify Backend Business Layer"
app.version = "1.0"

@app.get("/a", response_model=ResponseCoreAdapter)
def default():
    return EasyResponse.EasySuccessRespond( {"Info":"Victor Caxi All rights reserved" })

# Add Blockchain Services
app.include_router(ExampleController, prefix="/example-service-b/v1")
app.include_router(CustomerController, prefix="/customer/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")