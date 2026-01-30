from repositories.sales_repo import * 
from service.product_service import get_one_product 
from service.analitycs_service import service_post_a_user_online
from utils.access_token import decode_access_token
import uuid 
from fastapi.responses import JSONResponse
import mercadopago
import json


sdk = mercadopago.SDK("APP_USR-5708610925833516-012616-c46ac0af8146c4691ebc95ccf0d74968-443898421")


def service_create_sale(product_id:str,amount:int,value:float, user_cep:str,status:str,authorization:str, code:str, sizes:str,state:str,city:str, neighboor:str, street:str, complement:str ):

    decoded_token = decode_access_token(authorization)

    new_id = uuid.uuid4() 

    create_new_sale(str(new_id),decoded_token["sub"], product_id, amount,value, user_cep, status, code,sizes,state,city,neighboor,street,complement)
   

    return "criado com sucesso"

def service_del_cart_by_id(authorization:str, cart_id:str):

    token_decoded = decode_access_token(authorization)
    
    carts = get_carts_by_id(token_decoded["sub"])

    for cart in carts:
        if cart["id"] == cart_id:
            delete_sale_by_id(cart_id)
            return "iguaL"

    return JSONResponse(
        status_code = 404,
        content="produto não encontrado"
            )




def service_update_sale(authorization:str,sale_id:str, amount:int,value:float,user_cep:str, status:str, code:str, sizes:str,state:str,city:str, neighboor:str, street:str, complement:str):
    
    infos_sale = {"amount":amount, "value":value,"user_cep":user_cep,"status":status,"code":code,"sizes":sizes, "state":state,
                  "city":city,"neighboor":neighboor, "street":street, "complement":complement }

    
    if authorization == "admin":
       
        sale = get_sale_by_uuid(sale_id) 
            
        for key, value in infos_sale.items():
            if not value:
                
                infos_sale[key] = sale[0][key]

        put_sale( infos_sale["amount"],infos_sale["value"], infos_sale["user_cep"],infos_sale["status"],sale_id,infos_sale["code"], infos_sale["sizes"],infos_sale["state"],infos_sale["city"],infos_sale["neighboor"],infos_sale["street"],infos_sale["complement"])
        

        return infos_sale    
    

    decoded_token = decode_access_token(authorization)

    
    if decoded_token["role"] == "admin":
       
        sale = get_sale_by_uuid(sale_id) 
            
        for key, value in infos_sale.items():
            if not value:
                
                infos_sale[key] = sale[0][key]

        put_sale( infos_sale["amount"],infos_sale["value"], infos_sale["user_cep"],infos_sale["status"],sale_id,infos_sale["code"], infos_sale["sizes"],infos_sale["state"],infos_sale["city"],infos_sale["neighboor"],infos_sale["street"],infos_sale["complement"])
        

        return infos_sale    
        

    else:
        return "não autorizado"




    return "venda atualizada com sucesso"

def service_get_carts_by_id(authorization:str):

    decoded_token = decode_access_token(authorization)
    
    carts = get_carts_by_id(decoded_token["sub"])   

    return carts      


def service_take_checkout(user_id:str, products_id_list:list, amounts:list, user_cep:str, sizes:str, state:str, city:str, neighboor:str, street:str, complement:str):
 
    value_total = 0

    for product_id in products_id_list:
        product = get_one_product(product_id)
        
        value_total += product[0]["price"]

    print(value_total)
    json_data = json.dumps({"products_id":products_id_list, "products_amount":amounts})


    new_id = uuid.uuid4() 
    create_new_sale(str(new_id), user_id, json_data,value_total, user_cep, "aguardando pagamento",  sizes, state, city, neighboor, street, complement  )

    preference_data = {

            "items":[
                {
                    "items":"Alianças",
                    "quantity":1,
                    "unit_price":value_total

                }
                ],
            "external_reference":"iddealiancaseternas123",
            "back_urls":{
                     "success": "https://seusite.com/sucesso",
            "failure": "https://seusite.com/erro",
            "pending": "https://seusite.com/pendente"
                    },
                "auto_return":"approved"

            }

    preference = sdk.preference().create(preference_data)

    return preference["response"]["init_point"] 





