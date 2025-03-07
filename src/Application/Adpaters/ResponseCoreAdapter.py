from typing import Any, Optional
from Application.Adpaters.GlobalErrorCoreAdapter import GlobalErrorCoreAdapter
from pydantic import BaseModel, Field

class ResponseCoreAdapter (BaseModel):    
    status:int = Field(exclude=True)
    errors:list[GlobalErrorCoreAdapter] | None = None
    data:Any | None = None