from pydantic import BaseModel


class UserRequestAdapter(BaseModel):
    nombre: str
    apellido: str | None
