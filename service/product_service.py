from os import stat
import re
from typing import DefaultDict
import uuid
from repositories.products_repo import create_product, put_product,del_product, get_one_product, get_image_by_id, put_sale_of_one_product  
from utils.access_token import decode_access_token 
from datetime import datetime



def service_create_product(price:float, name:str,image_bytes:str,type:str,stone:int,material:str,checkout_link:str,authorization:str):
    
    decoded_token = decode_access_token(authorization)
    new_uuid = uuid.uuid4()

    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    if decoded_token["role"] == "admin":
           
        create_product(str(new_uuid),name, price, image_bytes, type, stone, material,checkout_link,formato_iso )

        return "concluido"

    else:
        return "não autorizado"




def service_update_product(price:float, name:str, image_binary:str,status:str,type:str, material:str,checkout_link:str, product_id:str, authorization:str):

    infos_produto = {"price":price,"name":name,"status":status, "type":type, "material":material, "checkout_link":checkout_link}

    now = datetime.now()


    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")
  
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
       
        product = get_one_product(product_id)
            
        if not image_binary:
            image_binary = get_image_by_id(product_id)

        for key, value in infos_produto.items():
            if not value:

                infos_produto[key] = product[0][key]

        put_product(infos_produto["name"],infos_produto["price"],formato_iso,image_binary,infos_produto["status"],infos_produto["type"],infos_produto["material"],infos_produto["checkout_link"],product_id) 
        

        return infos_produto    
        

    else:
        return "não autorizado"


def service_update_sales_of_product(commmand:int, product_id:str):

    if commmand == 1:

       product = get_one_product(product_id)
       put_sale_of_one_product(product[0]["sales"] + 1, product_id)
    return "ok" 



def service_delete_product(uuid:str, authorization:str):
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
           
        del_product(str(uuid))

        return "concluido"
        

    else:
        return "não autorizado"




