from Domain.Entities.HttpResponseEntity import HttpResponseEntity
import httpx

class HttpClientConnector:
    #*** Mantiene un solo AsyncClient para evitar abrir/cerrar conexiones constantemente.
    def __init__(self, timeout_sec: int = 15):        
        self.timeout_sec = timeout_sec
        self._client = httpx.AsyncClient(timeout=self.timeout_sec)

    #*** Cierra el AsyncClient, liberando recursos de red y sockets
    async def close(self):        
        await self._client.aclose()

    async def get_async(self, url: str, params=None, headers=None) -> HttpResponseEntity:
        response = await self._client.get(url, params=params, headers=headers)
        return self._build_response(response)

    async def post_async(self, url: str, data=None, params=None, headers=None) -> HttpResponseEntity:
        response = await self._client.post(url, json=data, params=params, headers=headers)
        return self._build_response(response)

    async def put_async(self, url: str, data=None, params=None, headers=None) -> HttpResponseEntity:
        response = await self._client.put(url, json=data, params=params, headers=headers)
        return self._build_response(response)

    #*** Convierte un httpx.Response en un HttpResponseEntity
    def _build_response(self, response: httpx.Response) -> HttpResponseEntity:
        try:
            content = response.json()
        except Exception:
            content = None

        return HttpResponseEntity(
            StatusCode=response.status_code,
            StatusContent=(content is not None),
            Content=content,
            Headers=response.headers,
            Url=str(response.url),
        )