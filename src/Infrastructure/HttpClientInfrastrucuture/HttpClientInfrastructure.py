from Domain.Entities.HttpResponseEntity import HttpResponseEntity
from Domain.Interfaces.IHttpClientInfrastructure import IHttpClientInfrastructure
from Infrastructure.HttpClientInfrastrucuture.HttpClientConnector import HttpClientConnector

# ********************************************************************************************************          
# * Copyright © 2025 Arify Labs - All rights reserved.   
# * 
# * Info                  : Build a http request Handler.
# *
# * By                    : Victor Jhampier Caxi Maquera
# * Email/Mobile/Phone    : victorjhampier@gmail.com | 968991*14
# *
# * Creation date         : 20/10/2024
# * 
# **********************************************************************************************************

class HttpClientInfrastructure(IHttpClientInfrastructure):
    def __init__(self):
        self.__ApiClient:HttpClientConnector = HttpClientConnector()        
        self.__base_url:str = ''
        self.__endpoint:str = ''
        self.__headers:dict = {}
        self.__params:dict = {}
        self.__query:dict = {}
    
    def timeout(self, timeout:int):
        self.__ApiClient.timeout_sec = timeout
        return self

    def http(self, base_url:str):
        self.__base_url = base_url
        return self

    def endpoint(self, endpoint:str):
        self.__endpoint = endpoint
        return self

    def header(self, key:str, value:str):
        self.__headers[key] = value
        return self
    
    def auth(self, key:str, value:str):
        self.__headers['Authorization'] = f"{key} {value}"
        return self
    
    def headers(self, headers:dict):        
        self.__headers.update(headers)
        return self

    def param(self, key:str, value:str):
        self.__params[key] = value
        return self
    
    def params(self, params:dict):
        self.__params.update(params)
        return self

    def query(self, key:str, value:str):
        self.__query[key] = value
        return self
    
    def queries(self, queries:dict):
        self.__query.update(queries)
        return self
    
    def __cleaner(self):
        if len(self.__headers) == 0:
            self.__headers['Content-Type'] ='application/json'
        
        self.__endpoint += '?' + '&'.join([f"{key}={value}" for key, value in self.__query.items()])
        return
        
    async def get(self) -> HttpResponseEntity:
        self.__cleaner()
        url = f"{self.__base_url}/{self.__endpoint}"
        return await self.__ApiClient.get_async(url, params=self.__params, headers=self.__headers)

    async def post(self, body:dict=None) -> HttpResponseEntity:
        self.__cleaner()
        url = f"{self.__base_url}/{self.__endpoint}"
        return await self.__ApiClient.post_async(url, data=body, params=self.__params, headers=self.__headers)

    async def put(self, body:dict=None) -> HttpResponseEntity:
        self.__cleaner()
        url = f"{self.__base_url}/{self.__endpoint}"
        return await self.__ApiClient.put_async(url, data=body, params=self.__params, headers=self.__headers)