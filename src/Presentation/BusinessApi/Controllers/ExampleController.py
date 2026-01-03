from Application.Adpaters.ExampleAdapters.CreateExampleAdapter import CreateExampleAdapter
from Application.Adpaters.ExampleAdapters.ExampleRequestAdaper import ExampleRequestAdaper
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Application.Usecases.ExampleCase.ExampleUsecase import ExampleUsecase
from Presentation.BusinessApi.Handlers.ArifyAuthorizer import ArifyAuthorizer
from Presentation.BusinessApi.Handlers.CognitoAuthorizer import CognitoAuthorizer
from Presentation.BusinessApi.Handlers.ScopesHandler import ScopesHandler
from Domain.Entities.Internals.MicroserviceCallTraceEntity import MicroserviceCallTraceEntity
from Presentation.BusinessApi.BusinessApiLogger import BusinessApiLogger
from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Containers.MemoryEvents.MicroserviceCallMemoryQueue import MicroserviceCallMemoryQueue

from fastapi import APIRouter, Security, Depends, Header, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from uuid import uuid4
import traceback

# Get the instance of the EasyResponseCoreHelper class
EasyResponse = EasyResponseCoreHelper()
ExampleController = APIRouter(tags=["Example"])
_logger = BusinessApiLogger.set_logger().getChild(__name__)

# Create a route for the get_user_for_example method
@ExampleController.post("/{customer_id}/create", response_model=CreateExampleAdapter)
async def get_user_for_example(    
    request: ExampleRequestAdaper, # Request Body
    customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
    include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
    auth: str = Header(..., title="Authorization", description="Token de autenticación"),
    usecase: ExampleUsecase = Depends(ExampleUsecase),  # Inyección directa de dependencia
    #_: dict = Security(ArifyAuthorizer(), scopes=[ScopesHandler.READ])
):
    _container: MicroserviceCallMemoryQueue = Services.get_instance(MicroserviceCallMemoryQueue)
    try:
        
        await _container.try_push(MicroserviceCallTraceEntity(
            Identity="user-983472",
            TraceId=str(uuid4()),
            ChannelId="MOBILE",
            DeviceId="ANDROID-PIXEL-7",
            Keyword="GetBalance",
            MicroserviceName="BusinessAPI2.0",
            OperationName="Transfer.GetBalance.execute",
            RequestUrl="/business-api/v2/transfer/get-balance",
            RequestHeader='{"Authorization":"Bearer eyJhbGciOi...","Content-Type":"application/json"}',
            RequestPayload='{"accountId":"1234567890","currency":"PEN"}',
            RequestDatetime=datetime.utcnow(),
            ResponseStatusCode=200,
            ResponsePayload='{"balance":1520.75,"currency":"PEN"}',
            ResponseDatetime=datetime.utcnow()
        ))
        _logger.info("Este es el codigo:"+str(customer_id) + 10)

        response: CreateExampleAdapter = await usecase.get_client_async(request)

        return JSONResponse(
            status_code=response.statusCode,
            content=jsonable_encoder(response, exclude_none=True)
        )
    
    except:
        _logger.error(traceback.format_exc().replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","No es de tu lado, es nuestro error"),exclude_none=True)
        )
# Create a route for the get_user_for_example method
@ExampleController.post("/{customer_id}/new/create", response_model=CreateExampleAdapter)
async def get_user_for_example2(    
    request: ExampleRequestAdaper, # Request Body
    customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
    include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
    auth: str = Header(..., title="Authorization", description="Token de autenticación"),
    usecase: ExampleUsecase = Depends(ExampleUsecase),  # Inyección directa de dependencia
    _: dict = Security(CognitoAuthorizer(), scopes=["openid"])
):
    try:
        response: CreateExampleAdapter = await usecase.get_client_async(request)

        return JSONResponse(
            status_code=response.statusCode,
            content=jsonable_encoder(response, exclude_none=True)
        )
    
    except:
        _logger.error(traceback.format_exc().replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","No es de tu lado, es nuestro error"),exclude_none=True)
        )