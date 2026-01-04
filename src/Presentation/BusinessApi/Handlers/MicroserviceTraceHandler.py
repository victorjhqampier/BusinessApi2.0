from typing import Any, Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from Presentation.BusinessApi.BusinessApiLogger import BusinessApiLogger
from Domain.Entities.Internals.MicroserviceCallTraceEntity import MicroserviceCallTraceEntity
from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Containers.MemoryEvents.MicroserviceCallMemoryQueue import MicroserviceCallMemoryQueue
from datetime import datetime
from uuid import uuid4

class MicroserviceTraceHandler:
    def __init__(self, request: Request, operation_name: str, keyword: str = "") -> None:
        self._container: MicroserviceCallMemoryQueue = Services.get_instance(MicroserviceCallMemoryQueue)
        self._logger = BusinessApiLogger.set_logger().getChild(self.__class__.__name__)
        self._request_datetime: datetime = datetime.utcnow()
        self._operation_name: str = operation_name
        self._keyword: str = keyword
        
        # Capturar información del request en el constructor
        headers = dict(request.headers)
        self._trace_id: str = headers.get("message-identification", "")
        self._channel_id: str = headers.get("channel-identification", "")
        self._device_id: str = headers.get("device-identification", "")
        self._request_url: str = str(request.url.path)
        self._method: str = request.method
        self._request_payload: Optional[str] = None

    async def initialize_request_body(self, request: Request) -> None:
        try:
            body_bytes = await request.body()
            if body_bytes:
                body_str = body_bytes.decode("utf-8", errors="replace")
                body_str = " ".join(body_str.split())  # Elimina saltos de línea y espacios extra
                self._request_payload = body_str[:1000] + "..." if len(body_str) > 1000 else body_str
        except Exception as e:
            self._logger.warning(f"Error capturando request body: {e}")
            self._request_payload = None

    async def capture_all(self, response: Any, status_code: int) -> None:                
        try:
            response_payload = jsonable_encoder(response)
            response_str = str(response_payload)
            # Limitar tamaño del payload de respuesta
            if len(response_str) > 2000:
                response_str = response_str[:2000] + "..."
        except Exception as e:
            self._logger.warning(f"Error serializando response: {e}")
            response_str = str(response)

        trace_entity = MicroserviceCallTraceEntity(
            Identity=str(uuid4()),
            TraceId=self._trace_id,
            ChannelId=self._channel_id,
            DeviceId=self._device_id,
            Keyword=self._keyword,
            Method=self._method,
            MicroserviceName="BusinessAPI2.0",
            OperationName=self._operation_name,
            RequestUrl=self._request_url,
            RequestPayload=self._request_payload,
            RequestDatetime=self._request_datetime,
            ResponseStatusCode=status_code,
            ResponsePayload=response_str,
            ResponseDatetime=datetime.utcnow()
        )

        await self._container.try_push(trace_entity)

    async def capture_error(self, error: Exception, status_code: int = 500) -> None:        
        error_message = str(error)
        if len(error_message) > 1000:
            error_message = error_message[:1000] + "..."

        trace_entity = MicroserviceCallTraceEntity(
            Identity=str(uuid4()),
            TraceId=self._trace_id,
            ChannelId=self._channel_id,
            DeviceId=self._device_id,
            Keyword=self._keyword,
            Method=self._method,
            MicroserviceName="BusinessAPI2.0",
            OperationName=self._operation_name,
            RequestUrl=self._request_url,
            RequestPayload=self._request_payload,
            RequestDatetime=self._request_datetime,
            ResponseStatusCode=status_code,
            ResponsePayload=f"ERROR: {error_message}",
            ResponseDatetime=datetime.utcnow()
        )

        await self._container.try_push(trace_entity)
