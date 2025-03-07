from Domain.Entities.HttpResponseEntity import HttpResponseEntity
import httpx

class HttpClientConnector():
    def __init__(self):
        self.timeout_sec = 15

    async def get_async(self, url:str, params=None, headers=None) -> HttpResponseEntity:   
        async with httpx.AsyncClient(timeout=self.timeout_sec) as client:            
            response = await client.get(url, params=params, headers=headers)
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

    async def post_async(self, url:str, data=None, params=None, headers=None) -> HttpResponseEntity:
        async with httpx.AsyncClient(timeout=self.timeout_sec) as client:            
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

    async def put_async(self, url:str, data=None, params=None, headers=None) -> HttpResponseEntity:
        async with httpx.AsyncClient(timeout=self.timeout_sec) as client:            
            response = await client.put(url, json=data, params=params, headers=headers)
            
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