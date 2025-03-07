from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

EasyResponse = EasyResponseCoreHelper()
BlockchainController = APIRouter(tags=["Blockchain"])

Logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
Logger.addHandler(console_handler)

@BlockchainController.get("/",response_model=ResponseCoreAdapter)
async def get_chain():
    try:
        data = {"hola":"date"}
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(data,exclude_none=True)
        )
    
    except Exception as ex:
        track:str = traceback.format_exc()
        Logger.error(track.replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
        )
    
@BlockchainController.post("/",response_model=ResponseCoreAdapter)
async def mine_chain():
    try:
        data = {"hola":"date"}
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(data,exclude_none=True)
        )
    
    except Exception as ex:
        track:str = traceback.format_exc()
        Logger.error(track.replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
        )