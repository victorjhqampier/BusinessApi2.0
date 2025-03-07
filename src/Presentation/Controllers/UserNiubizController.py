from Application.Interfaces.IClientNiubizCaseApplication import IClientNiubizCaseApplication
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Helpers.EasyResponseCoreHelper import EasyResponseCoreHelper
from Domain.Commons.DependencyContainer import get_dependency
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import traceback
import logging

EasyResponse = EasyResponseCoreHelper()
UserNiubizController = APIRouter(tags=["UserNiubiz"])

Logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
Logger.addHandler(console_handler)

@UserNiubizController.get("",response_model=ResponseCoreAdapter)
async def get_user_for_niubiz(CustomerCardIdentifier:int, CustomerCardNumber:str):
    try:
        # # Save Data for tracking
        # tracker:ILoggerApplication = get_dependency(ILoggerApplication)
        # id_tracker = tracker.open_log("client","get",{})

        data:IClientNiubizCaseApplication = get_dependency(IClientNiubizCaseApplication)
        response:ResponseCoreAdapter = await data.get_client(CustomerCardIdentifier,CustomerCardNumber)
        return JSONResponse(
            status_code=response.status,
            content=jsonable_encoder(response,exclude_none=True)
        )
    
    except Exception as ex:
        track:str = traceback.format_exc()
        Logger.error(track.replace('\n',' ').strip())
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(EasyResponse.EasyErrorRespond("99","Ocurrió el siguiente error: "+ str(ex)))
        )