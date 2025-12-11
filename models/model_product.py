from pydantic import BaseModel

class Request_create_product(BaseModel):
    name:str
    price:float
    image_url:str
    authorization:str

