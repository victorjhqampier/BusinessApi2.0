import json
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Application.Interfaces.ICustomerApplication import ICustomerApplication
from Application.Interfaces.ILoggerCoreApplication import ILoggerCoreApplication
from Domain.Commons.CoreServices import CoreServices as Services
from Application.Adpaters.ExampleAdapters.UserRequestAdapter import UserRequestAdapter


CustomerController = APIRouter(tags=['Customer'])

@CustomerController.post(path='/save',response_model=ResponseCoreAdapter)
async def Customer_save(UserRequest:UserRequestAdapter):
    try:
        customer_case:ICustomerApplication = Services.get_dependency(ICustomerApplication)  
        logger_case:ILoggerCoreApplication = Services.get_dependency(ILoggerCoreApplication)  
        idTrace = await logger_case.open_log(cApi='customer_register',cOperation='registrar_cliente',cJsonRequest=json.dumps(UserRequest.model_dump(),ensure_ascii=False))
        response:ResponseCoreAdapter = await customer_case.save(idTrace=idTrace) 
        await logger_case.close_log(idTrace,json.dumps(response.model_dump()))
        return JSONResponse(jsonable_encoder(response,exclude_defaults=True))
    except Exception as e:
        await logger_case.close_with_error_log(idTrace,{"Message": f"Salio un error: {str(e)}"})
        return JSONResponse({"Message": f"Salio un error: {str(e)}"})

@CustomerController.get(path='/register', response_model=ResponseCoreAdapter)
async def Customer_register(idTrace:str):
    try:
        customer_case:ICustomerApplication = Services.get_dependency(ICustomerApplication)  
        response:ResponseCoreAdapter = await customer_case.register(idTrace=idTrace)
        return JSONResponse(jsonable_encoder(response,exclude_defaults=True))
    except Exception as e:
        return JSONResponse({"Message": f"Salio un error: {str(e)}"})