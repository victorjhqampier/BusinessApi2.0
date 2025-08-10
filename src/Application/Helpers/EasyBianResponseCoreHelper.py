from typing import cast
from typing import Any, Type, TypeVar
from Application.Adpaters.Bians.FieldErrorBianCoreAdapter import FieldErrorBianCoreAdapter
from Application.Adpaters.Bians.ResponseBianCoreAdapter import ResponseBianCoreAdapter

T = TypeVar('T', bound=ResponseBianCoreAdapter)
class EasyBianResponseCoreHelper:

    def easy_error_respond(self, cErrorCode: str, cErrorMessage: str) -> ResponseBianCoreAdapter:
        objErrors:FieldErrorBianCoreAdapter = FieldErrorBianCoreAdapter(
            status_code=cErrorCode,
            status="ERROR",
            message=cErrorMessage
        )        
        return ResponseBianCoreAdapter(
            statusCode=500,            
            errors=[objErrors]
        )

    def easy_general_error_respond(self, _T: Type[T], errorList: list[FieldErrorBianCoreAdapter], nStatus=400) -> T:
        return _T(
            statusCode=nStatus,            
            errors=errorList
        )

    def easy_empty_respond(self, _T: Type[T], nStatus=204) -> T:
        return _T(
            statusCode=nStatus
        )

    def easy_success_respond(self, _T: Type[T], data_response: Any) -> T:
        result: T = _T(
            statusCode=200
        )
        for prop in _T.__annotations__.keys():
            if prop not in ["statusCode", "errors"]:                
                setattr(result, prop, data_response)
                break
        return cast(T, result)