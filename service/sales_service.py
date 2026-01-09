from repositories.sales_repo import create_new_sale,put_sale,get_sale_by_uuid, get_carts_by_id,delete_sale_by_id   
from service.product_service import service_update_product 
from utils.access_token import decode_access_token
import uuid 
from fastapi.responses import JSONResponse

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








