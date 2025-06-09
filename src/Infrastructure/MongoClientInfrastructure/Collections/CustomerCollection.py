from datetime import datetime
from pydantic import BaseModel


class CustomerCollection(BaseModel):
    _id: str | None
    cApellido: str | None
    cNombre: str | None
    dFechaRequest: datetime 
