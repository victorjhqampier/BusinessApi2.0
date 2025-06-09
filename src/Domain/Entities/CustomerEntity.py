from pydantic import BaseModel


class CustomerEntity(BaseModel):
    cApellido: str | None
    cNombre: str | None
