from Presentation.BusinessApi.BusinessApiLogger import BusinessApiLogger
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

class NoBianExampleController:
    def __init__(self) -> None:
        # ** Tener cuidado con el constructor, solo se llama una vez, es decir está en singlenthon **
        self.ApiRouter = APIRouter(tags=["ExampleNoBian"])       
        self._easy_response = EasyResponseCoreHelper()
        self._logger: logging.Logger = BusinessApiLogger.set_logger().getChild(__name__)        
        self.__my_routes()
    
    def __my_routes(self) -> None:
        self.ApiRouter.get("/", response_model=ResponseCoreAdapter)(self.get_example)
        self.ApiRouter.post("/", response_model=ResponseCoreAdapter)(self.push_example)
    
    async def get_example(self) -> JSONResponse:
        try:
            data: dict[str, str] = {"hola":"date"}
            return JSONResponse(
                status_code=200,
                content=jsonable_encoder(data,exclude_none=True)
            )
        
        except Exception as ex:
            track:str = traceback.format_exc()
            self._logger.error(track.replace('\n',' ').strip())
            return JSONResponse(
                status_code=500,
                content=jsonable_encoder(self._easy_response.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
            )
        
    async def push_example(self) -> JSONResponse:
        try:
            data: dict[str, str] = {"hola":"date"}
            return JSONResponse(
                status_code=200,
                content=jsonable_encoder(data,exclude_none=True)
            )
        
        except Exception as ex:
            track:str = traceback.format_exc()
            self._logger.error(track.replace('\n',' ').strip())
            return JSONResponse(
                status_code=500,
                content=jsonable_encoder(self._easy_response.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
            )

