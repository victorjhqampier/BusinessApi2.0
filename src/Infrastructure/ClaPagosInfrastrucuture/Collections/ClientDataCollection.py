from typing import Optional
from pydantic import BaseModel

class ClientDataCollection (BaseModel):
    idCliente:str
    cNombre:str
    cCorreo:str
    cNumeroTelefono:str
    dFechaRegistro:str
    nDiasRegistro:int