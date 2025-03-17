from Application.Adpaters.ExampleAdapters.CreateExampleAdapter import CreateExampleAdapter
from Application.Adpaters.ExampleAdapters.ExampleRequestAdaper import ExampleRequestAdaper
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Application.Usecases.ExampleCase.ExampleUsecase import ExampleUsecase
from Presentation.Handlers.ArifyAuthorizer import ArifyAuthorizer
from Presentation.Handlers.ScopesHandler import ScopesHandler
from fastapi import APIRouter, Security, Depends, Header, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

# Get the instance of the EasyResponseCoreHelper class
EasyResponse = EasyResponseCoreHelper()
ExampleController = APIRouter(tags=["Example"])


# initialize the logger
Logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
Logger.addHandler(console_handler)

# Create a route for the get_user_for_example method
@ExampleController.post("/{customer_id}/create", response_model=CreateExampleAdapter)
async def get_user_for_example(    
    request: ExampleRequestAdaper, # Request Body
    customer_id: int = Path(..., title="Customer ID", description="ID único del cliente"),
    include_details: bool = Query(False, title="Include Details", description="Si es True, devuelve más información"),
    auth: str = Header(..., title="Authorization", description="Token de autenticación"),
    usecase: ExampleUsecase = Depends(ExampleUsecase),  # Inyección de dependencia
    secury: dict = Security(ArifyAuthorizer(), scopes=[ScopesHandler.READ])
):
    try:
        response: CreateExampleAdapter = await usecase.get_client_async(request)

        return JSONResponse(
            status_code=response.statusCode,
            content=jsonable_encoder(response, exclude_none=True)
        )
    
    except Exception as ex:
        track:str = traceback.format_exc()
        Logger.error(track.replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
        )