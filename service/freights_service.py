from models import freight_models
from repositories.freights_repo import *
from utils.access_token import decode_access_token
from fastapi.responses import JSONResponse
import uuid


def service_get_freights(authorization:str):
    
    if authorization == None:
        response = JSONResponse(status_code = 401, content="Envie authorization pelo header")
        return response 
    
    decoded_token = decode_access_token(authorization)
  
    if decoded_token["role"] != "admin":
        return JSONResponse(status_code = 403, content="Sem autorização")


    response = get_freights_data() 


    return response

def service_create_freight(data:dict):
    
    decoded_token = decode_access_token(data.authorization)

    if decoded_token["role"] != "admin":
        return JSONResponse(status_code = 403, content="Sem autorização")

    new_id = uuid.uuid4() 

    create_row_freight(str(new_id),data.state, data.city, data.value )   


    return JSONResponse(status_code=201, content="frete adicionado")


def service_delete_row_freight(authorization:str, uuid:str):
    decoded_token = decode_access_token(authorization)
    print(decoded_token["role"])

    if decoded_token["role"] != "admin":
        return JSONResponse(status_code = 403, content="Sem autorização")


    del_row_freight(uuid)

    return JSONResponse(status_code=200, content="frete apagado")


def service_calculate_freight(state:str, city:str):
    
    freight_value = 0 
    freight = get_row_of_freight_by_city(city, state)

    if len(freight) > 0:
        freight_value = freight[0]["value"]   

    else:
        freight = get_row_of_freight_by_state(state)
     
        if len(freight) > 0:
            freight_value = freight[0]["value"]   

   
    return  freight_value









