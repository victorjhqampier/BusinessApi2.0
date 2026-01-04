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
from Presentation.BusinessApi.Handlers.MicroserviceTraceHandler import MicroserviceTraceHandler
from fastapi import APIRouter, Security, Depends, Header, Path, Query, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback

# Get the instance of the EasyResponseCoreHelper class
EasyResponse = EasyResponseCoreHelper()
ExampleController = APIRouter(tags=["Example"])
_logger = BusinessApiLogger.set_logger().getChild(__name__)

@ExampleController.post("/{customer_id}/create", response_model=CreateExampleAdapter)
async def get_user_for_example(
    http_request: Request,
    body: ExampleRequestAdaper, # Request Body
    customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
    include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
    auth: str = Header(..., title="Authorization", description="Token de autenticación"),
    usecase: ExampleUsecase = Depends(ExampleUsecase),  # Inyección directa de dependencia
    #_: dict = Security(ArifyAuthorizer(), scopes=[ScopesHandler.READ])
):
    # Inicializar trace handler con request info
    _easy_trace_handler = MicroserviceTraceHandler(
        request=http_request, 
        operation_name="getuser.forexample", 
        keyword="your_user_id"
    )
    
    try:
        # Inicializar body del request
        await _easy_trace_handler.initialize_request_body(http_request)
        
        response: CreateExampleAdapter = await usecase.get_client_async(body)

        # Capturar todo en una sola operación
        await _easy_trace_handler.capture_all(response=response, status_code=response.statusCode)
        
        return JSONResponse(
            status_code=response.statusCode,
            content=jsonable_encoder(response, exclude_none=True)
        )
    
    except Exception as e:        
        _logger.error(traceback.format_exc().replace('\n',' ').strip())
        # Capturar error
        await _easy_trace_handler.capture_error(error=e)
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","No es de tu lado, es nuestro error"),exclude_none=True)
        )


# Create a route for the get_user_for_example method
@ExampleController.post("/{customer_id}/new/create", response_model=CreateExampleAdapter)
async def get_user_for_example2(    
    body: ExampleRequestAdaper, # Request Body
    customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
    include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
    auth: str = Header(..., title="Authorization", description="Token de autenticación"),
    usecase: ExampleUsecase = Depends(ExampleUsecase),  # Inyección directa de dependencia
    _: dict = Security(CognitoAuthorizer(), scopes=["openid"])
):
    try:
        response: CreateExampleAdapter = await usecase.get_client_async(body)

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