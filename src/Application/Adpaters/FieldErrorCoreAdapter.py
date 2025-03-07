from typing import Optional
from pydantic import BaseModel

class FieldErrorCoreAdapter(BaseModel):
    code:int
    message:str
    field:Optional[str] = None