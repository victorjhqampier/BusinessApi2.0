from Application.Adpaters.GlobalErrorCoreAdapter import GlobalErrorCoreAdapter
from Application.Adpaters.ResponseCoreAdapter import ResponseCoreAdapter
from Domain.Enums.InternalHttpMenssage import InternalHttpMenssage

class EasyResponseCoreHelper:

    def EasyErrorRespond(self, cErrorCode: str, cErrorMessage: str, nStatus=500) -> ResponseCoreAdapter:
        objErrors:GlobalErrorCoreAdapter = GlobalErrorCoreAdapter(
            code=cErrorCode,
            message=cErrorMessage
        )        
        return ResponseCoreAdapter(            
            status=nStatus,            
            errors=[objErrors]
        )

    def EasyListErrorRespond(self, errorList: list, nStatus=400) -> ResponseCoreAdapter:
        return ResponseCoreAdapter(            
            status=nStatus,            
            errors=errorList
        )

    def EasyEmptyRespond(self) -> ResponseCoreAdapter:
        return ResponseCoreAdapter(            
            status=204
            # message=InternalHttpMenssage.SuccessEmpty if cMessage == None else cMessage
        )

    def EasySuccessRespond(self, dataResponse) -> ResponseCoreAdapter:
        return ResponseCoreAdapter(
            status=200,
            # message= InternalHttpMenssage.Success if cMessage == None else cMessage,
            data=dataResponse
        )