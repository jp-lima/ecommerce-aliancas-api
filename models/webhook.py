from pydantic import BaseModel, ConfigDict
from typing import Any, Dict

class Merchant(BaseModel):
    id: int
    alias: str

class WebhookYampi(BaseModel):
    event: str
    time: str
    merchant: Merchant
    resource: Dict[str, Any]

    model_config = ConfigDict(extra="allow")

class CustomerInfos(BaseModel):
    name:  str
    first_name:  str
    last_name: str 
    email: str
    cpf: str
     
    model_config = ConfigDict(extra = "allow")

    
