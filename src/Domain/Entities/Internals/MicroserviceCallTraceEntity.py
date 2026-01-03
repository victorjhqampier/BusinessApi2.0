from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MicroserviceCallTraceEntity (BaseModel):
    Identity: Optional[str] = None
    TraceId: str
    ChannelId: str
    DeviceId:str
    Keyword: Optional[str] = None
    MicroserviceName: str = "BusinessAPI2.0"  # This Project
    OperationName: str  # Transfer.GetBalance.execute
    RequestUrl: str
    RequestHeader: Optional[str] = None
    RequestPayload: Optional[str] = None
    RequestDatetime: datetime = datetime.now()
    ResponseStatusCode: int = 0
    ResponsePayload: Optional[str] = None
    ResponseDatetime: datetime = datetime.now()