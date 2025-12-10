from repositories.user_repo import get_all_users,get_user_by_email, post_new_user   
from utils.password import create_hash, verify_hash
from utils.access_token import create_access_token
import uuid
from datetime import datetime



def verify_password(email:str, password:str):
    user =  get_user_by_email(email)

    
    if verify_hash(password, user["password_hash"]):
        
        token = create_access_token(user["id"],user["name"],user["role"])

        return user | token
    else:
        return "email correto, mas a senha está errada"


def service_create_user (email:str, password:str, name:str):
    
    hashed_password = create_hash(password)
    new_uuid = uuid.uuid4()

    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    post_new_user(str(new_uuid), name,email, hashed_password, formato_iso, "")
 
    return "user criado"
