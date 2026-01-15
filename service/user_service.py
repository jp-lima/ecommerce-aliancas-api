from os import access, confstr
from fastapi.responses import JSONResponse
from repositories.user_repo import del_user, get_all_users,get_user_by_email, post_new_user, get_user_by_id, put_password  
from utils import access_token
from utils.password import create_hash, verify_hash
from utils.access_token import create_access_token, decode_access_token
from service.analitycs_service import service_add_new_estatistic_on_analitycs 
import uuid
from datetime import datetime



def verify_password(email:str, password:str):
    user =  get_user_by_email(email)
    
    if not user:

        return JSONResponse(
                    status_code=404,
                    content="Email não encontrado no banco de dados"

                )
    
    elif verify_hash(password, user["password_hash"]):
        
        token = create_access_token(user["id"],user["name"],user["role"])

        return JSONResponse(
                status_code=201,
                content={"username":user["name"],"role":user["role"],"user_id": user["id"], "access_token":token, }
                )
    else:
        return JSONResponse(
                status_code=401,
                content="Não autorizado"
                )

def service_update_password_user(authorization:str, new_password:str):
    
    access_token = decode_access_token(authorization)
    
    hashed_password = create_hash(new_password)

    put_password(hashed_password, access_token["sub"])


def service_get_all_users(authorization:str):

    access = decode_access_token(authorization)
    
    if(access["role"] == "admin"):

        all_users = get_all_users()

        return all_users
    else:
        return "não autorizado"

def service_create_user(email:str, password:str, name:str):
    
    hashed_password = create_hash(password)
    new_uuid = uuid.uuid4()

    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    post_new_user(str(new_uuid), name,email, hashed_password, formato_iso, "")

    service_add_new_estatistic_on_analitycs({"estatistic":"new_user", "data":""})

    return "user criado"



def service_delete_user(uuid:str, authorization:str):

    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
           
        del_user(str(uuid))

        return "concluido"
        

    else:
        return "não autorizado"

 





