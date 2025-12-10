from pydantic import BaseModel

class Request_new_sale(BaseModel):
    value:float
    product_id:str
    amount:int
    user_cep:str
    authorization:str
