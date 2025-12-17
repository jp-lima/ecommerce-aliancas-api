
from fastapi import APIRouter,Form,File, UploadFile,Response
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user, service_delete_user
from models.user import UserRequestLogin, UserCreateRequest, UserDeleteRequest    


router = APIRouter(
prefix="/users",
tags=["users"]
        )


# admin receber todos os usuários
@router.get("/")
def get_users():
    all_users = get_all_users()
    return all_users

@router.post("/auth")
def search_user(user:UserRequestLogin):
    response_login = verify_password(user.email,user.password) 

    return response_login

@router.post("/user/delete")
def delete_user(user:UserDeleteRequest):

    response = service_delete_user(user.user_id, user.authorization)

    return response 
    

# Qualquer pessoa criar novo usuário
@router.post("/create-user")
def create(user:UserCreateRequest):

    response = service_create_user(user.email, user.password, user.name)


    return response


