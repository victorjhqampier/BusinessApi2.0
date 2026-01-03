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
    def __init__(self) -> None:
        self._container: MicroserviceCallMemoryQueue = Services.get_instance(MicroserviceCallMemoryQueue)
        self.logger = BusinessApiLogger.set_logger().getChild(self.__class__.__name__)
        self._request: Optional[dict] = None

    async def capture_request(self, request: Request, operation_name:str, keyword: str = None) -> None:
        headers = dict(request.headers)
        body = None

        try:
            body_bytes = await request.body()
            if body_bytes:
                body_str = body_bytes.decode("utf-8", errors="replace")
                body_str = " ".join(body_str.split())  #elimina saltos de línea y espacios extra
                body = body_str[:1000] + "..." if len(body_str) > 1000 else body_str
        except Exception:
            body = None

        self._request = {
            "identity": str(uuid4()),
            "message_id": headers.get("message-identification", str(uuid4())),
            "device_id": headers.get("device-identification", "None"),
            "channel_id": headers.get("channel-identification", "None"),
            "url": str(request.url.path),
            "body": body
        }

        await self._container.try_push(MicroserviceCallTraceEntity(
            Identity=self._request["identity"],
            TraceId=self._request["message_id"],
            ChannelId=self._request["channel_id"],
            DeviceId=self._request["device_id"],
            Keyword=keyword,
            MicroserviceName="BusinessAPI2.0",
            OperationName=operation_name,  # Example: Transfer.GetBalance.execute
            RequestUrl=self._request["url"],
            RequestPayload=self._request["body"]
        ))

    async def capture_response(self, response: Any, status_code: int) -> None:
        response_parsed = jsonable_encoder(response)
        await self._container.try_push(MicroserviceCallTraceEntity(
            Identity=self._request["identity"],
            TraceId="",
            ChannelId="",
            DeviceId="",
            Keyword="",
            MicroserviceName="",
            OperationName="",
            RequestUrl="",
            ResponseStatusCode=status_code,
            ResponsePayload=str(response_parsed),
            ResponseDatetime=datetime.utcnow()
        ))

#     async def capture_error(self, error: Any, stack_trace: Any = None) -> None:
#         error_parsed = _to_jsonable(error)
#         payload = {"error": error_parsed}
#         if stack_trace is not None:
#             payload["stack_trace"] = str(stack_trace)
#         self._log_data(payload)

#     def _log_data(self, data: Any) -> None:
#         try:
#             self.logger.info("MICROSERVICE TRACE DATA: %s", json.dumps(data))
#         except Exception:
#             self.logger.info("MICROSERVICE TRACE DATA: %s", str(data))


# def _to_jsonable(obj: Any) -> Any:
#     try:
#         if hasattr(obj, "model_dump"):
#             return obj.model_dump()
#         if hasattr(obj, "dict"):
#             return obj.dict()
#         return json.loads(json.dumps(obj, default=str))
#     except Exception:
#         return str(obj)
#                 error_str = json.dumps(error.model_dump())
