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

async def delete_image_from_supabase(image_url:str):

    image_name = image_url.split("/")
       
    response = supabase.storage.from_("products").remove([image_name[-1]])

    return


async def service_create_product(price:float, name:str,image_bytes:str,image2_bytes:str,image3_bytes:str,type:str,stone:int,material:str,checkout_link:str,authorization:str, image, image2, image3 ):
    
    image_url = await upload_image_to_supabase(image_bytes, image, image.filename)

    image2_url = await upload_image_to_supabase(image2_bytes, image2, image2.filename) if image2 else ""

    image3_url = await upload_image_to_supabase(image3_bytes, image3, image3.filename) if image3 else ""



    decoded_token = decode_access_token(authorization)
    new_uuid = uuid.uuid4()

    now = datetime.now(ZoneInfo("America/Sao_Paulo"))

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    if decoded_token["role"] == "admin":
           
        create_product(str(new_uuid),name, price, image_url, image2_url, image3_url, type, stone, material,checkout_link,formato_iso )

        return JSONResponse(status_code=201,content="produto criado")

    else:
        return JSONResponse(status_code=401, content="Não autorizado") 


def service_get_image_for_product(uuid:str, index:int):

    image = get_image_by_id(uuid)

    if not image[index -1]:
        return "Não encontrado" 

    return image[ index - 1] 




async def service_update_product(price:float, name:str, image,image2,image3,status:str,type:str, material:str,checkout_link:str, product_id:str, authorization:str):

    infos_produto = {"price":price,"name":name,"status":status, "type":type, "material":material, "checkout_link":checkout_link}
    images = {"image_url":image, "image2_url":image2,"image3_url":image3}
    images_url = {"image_url":"", "image2_url":"", "image3_url":""}

    now = datetime.now()


    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")
  
    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
       
        product = get_one_product(product_id)

       # se já estiver uma image_url no product apagar a imagem do supabase e adicionar uma nova e trocar url da coluna
       # Se não tiver url, adicionar uma nova url e uma nova foto
       # $$$$$$-Se não for pedido, continuar mesma url-
        images_url["image_url"] = product[0]["image_url"] 
        images_url["image2_url"]  = product[0]["image2_url"] 
        images_url["image3_url"]  = product[0]["image3_url"] 


        for key, value in images.items():
            if value:
                if product[0][key]:
                    response_delete = await delete_image_from_supabase(product[0][key])
                      
                image_content = await value.read();
                print("foto enviada", image_content)
                image_url = await upload_image_to_supabase(image_content, value, value.filename)
                images_url[key] = image_url
        

        for key, value in infos_produto.items():
            if not value:

                infos_produto[key] = product[0][key]

        put_product(infos_produto["name"],infos_produto["price"],formato_iso,images_url["image_url"],images_url["image2_url"],
       images_url["image3_url"],infos_produto["status"],infos_produto["type"],infos_produto["material"],infos_produto["checkout_link"],product_id) 
        

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





