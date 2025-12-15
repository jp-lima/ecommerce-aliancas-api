from repositories.sales_repo import create_new_sale,put_sale,get_line_by_uuid  
from utils.access_token import decode_access_token
import uuid 


def service_create_sale(product_id:str,amount:int,value:float, user_cep:str,status:str,authorization:str):

    decoded_token = decode_access_token(authorization)

    new_id = uuid.uuid4() 

    create_new_sale(str(new_id),decoded_token["sub"], product_id, amount,value, user_cep, status)
    

    return "criado com sucesso"

def service_update_sale(authorization:str,product_id:str, amount:int,value:float,user_cep:str, status:str):

    decoded_token = decode_access_token(authorization)
     
    sale = get_line_by_uuid(product_id) 
    
    if len(sale) == 0:
        return "não tem venda com esse id"
    
    else:

        put_sale(decoded_token["sub"], product_id, amount,value, user_cep,status,sale[0]["id"])

        return "venda atualizada com sucesso"
       
