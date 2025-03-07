from Domain.Entities.HttpResponseEntity import HttpResponseEntity
from Domain.Interfaces.IAuthServerInfrastructure import IAuthServerInfrastructure
import httpx

class CognitoAutorizationCognito(IAuthServerInfrastructure):
    def __init__(self):
        self.__timeout=15

    async def post_async(self, url:str, data=None, params=None, headers=None) -> HttpResponseEntity:
        async with httpx.AsyncClient(timeout=self.__timeout) as client:            
            response = await client.post(url, json=data, params=params, headers=headers)
            try:
                content = response.json()
            except:
                content = None

            return HttpResponseEntity(
                StatusCode=response.status_code,
                StatusContent = content is not None,
                Content=content,
                Headers=response.headers,
                Url=str(response.url)
            )
