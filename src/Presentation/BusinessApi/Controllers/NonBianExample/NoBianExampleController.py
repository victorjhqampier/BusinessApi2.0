from Presentation.BusinessApi.BusinessApiLogger import BusinessApiLogger
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

EasyResponse = EasyResponseCoreHelper()
NoBianExampleController = APIRouter(tags=["ExampleNoBian"])

Logger: Logger = BusinessApiLogger.set_logger().getChild(__name__)

@NoBianExampleController.get("/",response_model=ResponseCoreAdapter)
async def get_example() -> JSONResponse:
    try:
        data: dict[str, str] = {"hola":"date"}
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
    
@NoBianExampleController.post("/",response_model=ResponseCoreAdapter)
async def push_example() ->JSONResponse:
    try:
        data: dict[str, str] = {"hola":"date"}
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