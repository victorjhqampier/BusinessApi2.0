from Domain.Interfaces.IClientInfrastructure import IClientInfrastructure
from Domain.Entities.Client.ClientNiubizEntity import ClientNiubizEntity
from Domain.Entities.Client.ClientResponseEntity import ClientResponseEntity
from Application.Adpaters.GlobalErrorCoreAdapter import GlobalErrorCoreAdapter
from Application.Interfaces.IAuthServerCoreApplication import IAuthServerCoreApplication
from Domain.Commons.DependencyContainer import get_dependency
from Infrastructure.ClaPagosInfrastrucuture.ClaPagosSetting import ClaPagosSetting
from Domain.Entities.HttpResponseEntity import HttpResponseEntity

class ClientCommand (IClientInfrastructure):    
    def __init__(self) -> None:
        self.__builder_api_client:IHttpClientCoreApplication = get_dependency(IHttpClientCoreApplication)
        self.__cognito_token : IAuthServerCoreApplication = get_dependency(IAuthServerCoreApplication)
    
    async def get_client(self,CustomerCardIdentifier:int, CustomerCardNumber:str) -> ClientResponseEntity:
        jwt:str = await self.__cognito_token.get_cognito_token()
        
        self.__builder_api_client.http(ClaPagosSetting.URL_BASE.value
                            ).endpoint(ClaPagosSetting.PATH_NIUBIZ_CLIENT.value
                            ).queries({"idTipoDocumento":CustomerCardIdentifier,"cDocumento":CustomerCardNumber}
                            ).auth("Bearer", jwt)
        
        result:HttpResponseEntity = await self.__builder_api_client.get()

        if len(result.Content) == 0:
            raise ValueError("Resource Server send a exception : "+ result.Url)

        # if(result.StatusCode != 200 or result.Content["success"] != 1):
        #     result.Content["success"] = 0

        # data = ClientDataCollection(**result.Content["data"]) if len(result.Content["data"]) > 0 else None
        return ClientResponseEntity(
            data = ClientNiubizEntity (
                CustomerIdentifier = result.Content["data"]["idCliente"],
                CustomerName=result.Content["data"]["cNombre"],
                CustomerEmail = result.Content["data"]["cCorreo"],
                CustomerPhoneNumber = result.Content["data"]["cNumeroTelefono"],
                RegistrationDate = result.Content["data"]["dFechaRegistro"],
                DaysSinceRegistration= result.Content["data"]["nDiasRegistro"]
            ) if len(result.Content["data"]) > 0 else None,
            errors = [GlobalErrorCoreAdapter(**item) for item in result.Content["errors"]] if len(result.Content["errors"]) > 0 else None
        )