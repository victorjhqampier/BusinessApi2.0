from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.CoreApplicationSetting import CoreApplicationSetting
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Presentation.Controllers.BlockchainController import BlockchainController
from fastapi import FastAPI
import uvicorn

# ********************************************************************************************************          
# * Copyright © 2024 Victor Jhampier Caxi - All rights reserved.   
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

app = FastAPI(docs_url="/docs/openapi", redoc_url="/docs/reopenapi")
app.title = "Arix blockchain"
app.version = "1.0"

@app.get("/", response_model=ResponseCoreAdapter)
def default():
    return EasyResponse.EasySuccessRespond( {"Info":"Victor Caxi All rights reserved" })

# Add Blockchain Services
app.include_router(BlockchainController, prefix="/api/blockchain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")