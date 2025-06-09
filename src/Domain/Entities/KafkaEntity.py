from pydantic import BaseModel

class KafkaEntity(BaseModel):
    idTrace:str
    nIntentos:int
    
    