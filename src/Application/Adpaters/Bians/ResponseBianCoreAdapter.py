from Application.Adpaters.Bians.FieldErrorBianCoreAdapter import FieldErrorBianCoreAdapter
from pydantic import BaseModel, Field

class ResponseBianCoreAdapter (BaseModel):    
    statusCode:int = Field(exclude=True)
    errors:list[FieldErrorBianCoreAdapter] | None = None
    # AQUI DEBE IR TU RESPONSE