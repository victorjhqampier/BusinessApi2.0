from Presentation.BusinessApi.Models.RequestInputModel import RequestInputModel
from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Containers.MemoryEvents.MicroserviceCallMemoryQueue import MicroserviceCallMemoryQueue
from Application.Adpaters.ExampleAdapters.CreateExampleAdapter import CreateExampleAdapter
from Application.Adpaters.ExampleAdapters.ExampleRequestAdaper import ExampleRequestAdaper
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Application.Usecases.ExampleCase.ExampleUsecase import ExampleUsecase
from Presentation.BusinessApi.Handlers.CognitoAuthorizer import CognitoAuthorizer
from Presentation.BusinessApi.BusinessApiLogger import BusinessApiLogger
from Presentation.BusinessApi.Handlers.MicroserviceTraceHandler import MicroserviceTraceHandler
from fastapi import APIRouter, Security, Depends, Header, Path, Query, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

class BianExampleController:
    def __init__(self) -> None:
        # ** Tener cuidado con el constructor, solo se llama una vez, es decir está en singlenthon **
        self.ApiRouter = APIRouter(tags=["BIAN Example"])
        self._easy_response = EasyResponseCoreHelper()
        self._logger: logging.Logger = BusinessApiLogger.set_logger().getChild(__name__)
        self.__my_routes()
    
    def __my_routes(self) -> None:
        self.ApiRouter.post("/{customer_id}/create", response_model=CreateExampleAdapter)(self.get_user_for_example)
        self.ApiRouter.post("/{customer_id}/new/create", response_model=CreateExampleAdapter)(self.get_user_for_example2)
    
    async def get_user_for_example(
        self,
        http_request: Request,
        body: ExampleRequestAdaper,
        customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
        include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
        auth: str = Header(..., title="Authorization", description="Token de autenticación"),
        usecase: ExampleUsecase = Depends(ExampleUsecase)
    ) -> JSONResponse:
        queue_sender: MicroserviceTraceHandler = MicroserviceTraceHandler(Services.get_instance(MicroserviceCallMemoryQueue))
        request_data:RequestInputModel = RequestInputModel(request=http_request, operation_name="obtener-cliente", keyword=customer_id)
        
        try:            
            result: CreateExampleAdapter = await usecase.get_client_async(body)

            await queue_sender.push_success(request_data, response=result, status_code=result.statusCode)            
            return JSONResponse(
                status_code=result.statusCode,
                content=jsonable_encoder(result, exclude_none=True)
            )
        
        except Exception as e:        
            self._logger.error(str(e) + " in "+traceback.format_exc().replace('\n',' ').strip())
            await queue_sender.push_error(request_data, error=e)
            return JSONResponse(
                status_code=500,
                content=jsonable_encoder(self._easy_response.EasyErrorRespond("99","No es de tu lado, es nuestro error"),exclude_none=True)
            )

    async def get_user_for_example2(
        self,
        http_request: Request,
        body: ExampleRequestAdaper,
        customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
        include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
        auth: str = Header(..., title="Authorization", description="Token de autenticación"),
        usecase: ExampleUsecase = Depends(ExampleUsecase),
        _: dict = Security(CognitoAuthorizer(), scopes=["openid"])
    ) -> JSONResponse:
        queue_sender: MicroserviceTraceHandler = MicroserviceTraceHandler(Services.get_instance(MicroserviceCallMemoryQueue))
        request_data:RequestInputModel = RequestInputModel(request=http_request, operation_name="obtener-cliente-otros", keyword=customer_id)
        
        try:
            response: CreateExampleAdapter = await usecase.get_client_async(body)
            await queue_sender.push_success(request_data,response=response, status_code=response.statusCode)
            return JSONResponse(
                status_code=response.statusCode,
                content=jsonable_encoder(response, exclude_none=True)
            )
        
        except Exception as e:
            self._logger.error(str(e) + " in "+traceback.format_exc().replace('\n',' ').strip())
            await queue_sender.push_error(request_data, error=e)
            return JSONResponse(
                status_code=500,
                content=jsonable_encoder(self._easy_response.EasyErrorRespond("99","No es de tu lado, es nuestro error"),exclude_none=True)
            )

