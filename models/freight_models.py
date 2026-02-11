from pydantic import BaseModel


class Request_Create_Freight(BaseModel):
    authorization:str
    state:str
    city:str | None = None 
    value:float

class Request_Get_Freight(BaseModel):
    state:str
    city:str










