from os import stat
import re
from typing import DefaultDict
import uuid
from repositories import products_repo
from repositories.products_repo import create_product, put_product,del_product
from utils.access_token import decode_access_token 
from datetime import datetime



def service_create_product(price:float, name:str, image_url:str, authorization:str):
    # criar id, verificar access_token
    
    decoded_token = decode_access_token(authorization)
    new_uuid = uuid.uuid4()

    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    if decoded_token["role"] == "admin":
            
        create_product(str(new_uuid),name, price, image_url, formato_iso )

        return "concluido"
        

    else:
        return "não autorizado"




    #return decoded_token["role"]

def service_update_product(price:float, name:str, image_url:str,status:str,product_id:str, authorization:str):
   
    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
            
        put_product(name,price,formato_iso, image_url,status,product_id) 

        return "concluido"
        

    else:
        return "não autorizado"

def service_delete_product(uuid:str, authorization:str):
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
           
        del_product(str(uuid))

        return "concluido"
        

    else:
        return "não autorizado"

 




