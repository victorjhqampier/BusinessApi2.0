from typing import Dict, Optional
from Domain.Entities.HttpResponseEntity import HttpResponseEntity
from Domain.Interfaces.IHttpClientInfrastructure import IHttpClientInfrastructure
from Infrastructure.HttpClientInfrastrucuture.HttpClientConnector import HttpClientConnector
from Domain.Commons.CoreServices import CoreServices as Services

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
        self.__ApiClient: HttpClientConnector = Services.get_instance(HttpClientConnector)
        self.__base_url: str = ''
        self.__endpoint: str = ''
        self.__headers: dict = {}
        self.__params: dict = {}
        self.__query: dict = {}

    def timeout(self, timeout: int) -> "HttpClientInfrastructure":
        # No está en la interfaz, pero es adicional si lo deseas
        self.__ApiClient.timeout_sec = timeout
        return self

    def http(self, base_url: str) -> "HttpClientInfrastructure":
        self.__base_url = base_url.rstrip('/')
        return self

    def endpoint(self, endpoint: str) -> "HttpClientInfrastructure":
        self.__endpoint = endpoint.lstrip('/')
        return self

    def header(self, key: str, value: str) -> "HttpClientInfrastructure":
        self.__headers[key] = value
        return self

    def authorization(self, key: str, value: str) -> "HttpClientInfrastructure":
        # Método adicional, no en la interfaz
        self.__headers['Authorization'] = f"{key} {value}"
        return self

    def headers(self, headers: Dict[str, str]) -> "HttpClientInfrastructure":
        self.__headers.update(headers)
        return self

    def param(self, key: str, value: str) -> "HttpClientInfrastructure":
        self.__params[key] = value
        return self

    def params(self, params: Dict[str, str]) -> "HttpClientInfrastructure":
        self.__params.update(params)
        return self

    def query(self, key: str, value: str) -> "HttpClientInfrastructure":
        self.__query[key] = value
        return self

    def queries(self, queries: Dict[str, str]) -> "HttpClientInfrastructure":
        self.__query.update(queries)
        return self

    def _build_final_url(self) -> str:
        path = f"{self.__base_url}/{self.__endpoint}"
        if self.__query:
            qs = '&'.join(f"{k}={v}" for k, v in self.__query.items())
            return f"{path}?{qs}"
        return path

    def _ensure_default_headers(self) -> None:
        if not self.__headers:
            self.__headers['Content-Type'] = 'application/json'

    async def get(self) -> HttpResponseEntity:
        self._ensure_default_headers()
        final_url = self._build_final_url()
        return await self.__ApiClient.get_async(
            url=final_url, 
            params=self.__params,
            headers=self.__headers
        )

    async def post(self, body: Optional[dict] = None) -> HttpResponseEntity:
        self._ensure_default_headers()
        final_url = self._build_final_url()
        return await self.__ApiClient.post_async(
            url=final_url,
            data=body,
            params=self.__params,
            headers=self.__headers
        )

    async def put(self, body: Optional[dict] = None) -> HttpResponseEntity:
        self._ensure_default_headers()
        final_url = self._build_final_url()
        return await self.__ApiClient.put_async(
            url=final_url,
            data=body,
            params=self.__params,
            headers=self.__headers
        )

    async def close(self) -> None:
        await self.__ApiClient.close()