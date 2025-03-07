from typing import Optional
from pydantic import BaseModel

class GlobalErrorCoreAdapter(BaseModel):
    code:int
    message:str
    field:Optional[str] = None