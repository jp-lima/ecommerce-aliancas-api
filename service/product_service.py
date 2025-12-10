from typing import DefaultDict
import uuid
from repositories.products_repo import create_product
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




