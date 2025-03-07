from typing import Optional
from pydantic import BaseModel

class FieldErrorBianCoreAdapter(BaseModel):
    status_code:str
    message:Optional[str] = None
    status: Optional[str] = None