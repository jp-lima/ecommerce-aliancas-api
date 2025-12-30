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

