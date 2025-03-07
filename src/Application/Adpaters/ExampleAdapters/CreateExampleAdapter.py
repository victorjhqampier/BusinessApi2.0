from typing import Optional
from Application.Adpaters.Bians.ResponseBianCoreAdapter import ResponseBianCoreAdapter
from pydantic import BaseModel, Field

class CreateExampleAdapter(ResponseBianCoreAdapter):
    createExampleResponse: Optional["CreateExampleResponse"] = None

class CreateExampleResponse(BaseModel):
    name:str = Field(..., title="Name", description="Name of the example")
    age:int = Field(..., title="Age", description="Age of the example")
    email:Optional[str] = Field(..., title="Email", description="Email of the example")
