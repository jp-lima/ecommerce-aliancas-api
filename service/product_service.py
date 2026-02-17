from os import stat
from fastapi.responses import JSONResponse
import re
from typing import DefaultDict
import uuid
from repositories.products_repo import * 
from utils.access_token import decode_access_token 
from datetime import datetime
from zoneinfo import ZoneInfo
from supabase import create_client

SUPABASE_URL = "https://qqxlznjxpekbpqblakju.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFxeGx6bmp4cGVrYnBxYmxha2p1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NTI1NDA3NiwiZXhwIjoyMDgwODMwMDc2fQ.WxjRhGDUNKblTFvmEO5nJn2ODrvA2o_NE29cYaNCISU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def upload_image_to_supabase(file_content,file, file_name):

#    file_content = await file.read()
#    print(file_content, "file_content")
#    file_name = file.filename

    response = supabase.storage.from_("products").upload(
        file_name,
        file_content,
        {"content-type": file.content_type}
    )

    public_url = supabase.storage.from_("products").get_public_url(file_name)

    return public_url




async def service_create_product(price:float, name:str,image_bytes:str,image_2bytes:str,image3_bytes:str,image4_bytes:str,type:str,stone:int,material:str,checkout_link:str,authorization:str, image:str ):
    
    image_url = await upload_image_to_supabase(image_bytes, image, image.filename)

    decoded_token = decode_access_token(authorization)
    new_uuid = uuid.uuid4()

    now = datetime.now(ZoneInfo("America/Sao_Paulo"))

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    if decoded_token["role"] == "admin":
           
        create_product(str(new_uuid),name, price, image_url, image_bytes, image_2bytes, image3_bytes, image4_bytes, type, stone, material,checkout_link,formato_iso )

        return JSONResponse(status_code=201,content="produto criado")

    else:
        return JSONResponse(status_code=401, content="Não autorizado") 


def service_get_image_for_product(uuid:str, index:int):

    image = get_image_by_id(uuid)

    if not image[index -1]:
        return "Não encontrado" 

    return image[ index - 1] 




def service_update_product(price:float, name:str, image_binary:str,image2_binary:str,image3_binary:str,image4_binary:str,status:str,type:str, material:str,checkout_link:str, product_id:str, authorization:str):

    infos_produto = {"price":price,"name":name,"status":status, "type":type, "material":material, "checkout_link":checkout_link}

    now = datetime.now()


    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")
  
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
       
        product = get_one_product(product_id)
            
        if not image_binary:
            image_binary = service_get_image_for_product(product_id, 1)
       
        if not image2_binary:
            image2_binary = service_get_image_for_product(product_id, 2)
        
        if not image3_binary:
            image3_binary = service_get_image_for_product(product_id, 3)

        if not image4_binary:
            image4_binary = service_get_image_for_product(product_id, 4)


        for key, value in infos_produto.items():
            if not value:

                infos_produto[key] = product[0][key]

        put_product(infos_produto["name"],infos_produto["price"],formato_iso,image_binary,image2_binary,image3_binary,image4_binary,infos_produto["status"],infos_produto["type"],infos_produto["material"],infos_produto["checkout_link"],product_id) 
        

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





