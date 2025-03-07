from abc import ABC, abstractmethod

from Domain.Entities.HttpResponseEntity import HttpResponseEntity

class IHttpClientInfrastructure(ABC):
    @abstractmethod
    def http(self, base_url:str):
        pass

    @abstractmethod
    def endpoint(self, endpoint:str):
        pass

    @abstractmethod
    def header(self, key:str, value:str):
        pass

    @abstractmethod
    def auth(self, key:str, value:str):
        pass

    @abstractmethod
    def headers(self, headers:dict):
        pass

    @abstractmethod
    def param(self, key:str, value:str):
        pass

    @abstractmethod
    def params(self, params:dict):
        pass

    @abstractmethod
    def query(self, key:str, value:str):
        pass

    @abstractmethod
    def queries(self, queries:dict):
        pass

    @abstractmethod
    async def get(self) -> HttpResponseEntity:
        pass

    @abstractmethod
    async def post(self, body=None) -> HttpResponseEntity:
        pass

    @abstractmethod
    async def put(self, body=None) -> HttpResponseEntity:
        pass