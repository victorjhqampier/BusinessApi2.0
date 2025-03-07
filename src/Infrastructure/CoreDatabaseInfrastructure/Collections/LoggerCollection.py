from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class LoggerCollection (BaseModel):
    _id:str | None = None
    idPadre:Optional[str]
    cApi:str
    cOperation:str
    ckeywords:str | None
    dFechaRequest:datetime
    cJsonRequest:str
    dFechaResponse:datetime | None
    cJsonResponse:str | None
    lIsSuccess:bool = False
    