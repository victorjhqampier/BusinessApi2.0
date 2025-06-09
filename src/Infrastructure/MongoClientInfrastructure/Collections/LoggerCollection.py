from datetime import datetime
from pydantic import BaseModel


class LoggerCollection(BaseModel):
    _id: str | None
    idPadre: str | None = None
    cApi: str | None = None
    cOperation: str
    identityNumber: int | None = None
    externalId: str | None = None
    ckeywords: str | None = None
    dFechaRequest: datetime
    cJsonRequest: str
    dFechaResponse: datetime | None = None
    cJsonResponse: str | None = None
    lIsSuccess: bool = False
