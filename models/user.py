from pydantic import BaseModel

class UserRequestLogin(BaseModel):
    email:str
    password:str
    
class UserCreateRequest(BaseModel):
    name:str
    email:str
    password:str
    phone:str

class UserDeleteRequest(BaseModel):
    user_id:str
    authorization:str

class RequestGetAuthorization(BaseModel):
    authorization:str

class RequestNewPassword(BaseModel):
    authorization:str
    new_password:str


