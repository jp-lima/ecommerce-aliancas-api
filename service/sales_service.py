from repositories.sales_repo import create_new_sale 
from utils.access_token import decode_access_token
import uuid 


def service_create_sale(product_id:str,amount:int,value:float, user_cep:str,authorization:str):

    decoded_token = decode_access_token(authorization)

    new_id = uuid.uuid4() 

    create_new_sale(str(new_id),decoded_token["sub"], product_id, amount,value, user_cep, "encomendado")
    

    return "criado com sucesso"


