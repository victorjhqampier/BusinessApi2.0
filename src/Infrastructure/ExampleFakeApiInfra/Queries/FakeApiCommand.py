from typing import Optional
from Domain.Entities.ExampleFakeApi.FakeApiEntity import FakeApiEntity
from Application.Adpaters.GlobalErrorCoreAdapter import GlobalErrorCoreAdapter
from Domain.Commons.DependencyContainer import get_dependency
from Domain.Interfaces.IFakeApiInfrastructure import IFakeApiInfrastructure
from Domain.Interfaces.IHttpClientInfrastructure import IHttpClientInfrastructure
from Domain.Entities.HttpResponseEntity import HttpResponseEntity
from Infrastructure.ExampleFakeApiInfra.ExampleFakeApiSetting import ExampleFakeApiSetting
import logging

class FakeApiCommand (IFakeApiInfrastructure):
    def __init__(self) -> None:
        self.__builder_api_client:IHttpClientInfrastructure = get_dependency(IHttpClientInfrastructure)
        
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)
        if not self.__logger.hasHandlers():
            self.__logger.addHandler(console_handler)
    
    async def get_user_async(self,id:int) -> Optional[FakeApiEntity]:    
        self.__builder_api_client.http(ExampleFakeApiSetting.EXAMPLE_HOST_BASE.value).endpoint(f"todos/{id}")
        
        result:HttpResponseEntity = await self.__builder_api_client.get()

        if result.StatusCode == 500 or not result.Content:
            self.__logger.error(f"[{result.StatusCode}] [{result.Url}] : {str(result.Content)}")
            return None

        if result.StatusCode != 200:
            self.__logger.warning(f"[{result.StatusCode}] [{result.Url}] - {str(result.Content)}")
            return None

        return FakeApiEntity(
                userId = result.Content.get("userId", 0),
                id = result.Content.get("id", 0),
                title = result.Content.get("title", "No Title"),
                completed = result.Content.get("completed", False)
        )