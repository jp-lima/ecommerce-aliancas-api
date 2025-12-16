import re
from warnings import resetwarnings
from models import user
from repositories import products_repo
from fastapi import FastAPI, UploadFile, File, Form,Response 
from db import get_conn
from pydantic import BaseModel 
from repositories.products_repo import get_all_products, get_image_by_id, get_one_product
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user, service_delete_user
from service.product_service import service_create_product, service_delete_product, service_update_product
from models.user import UserRequestLogin, UserCreateRequest, UserDeleteRequest    
from models.model_product import Request_create_product, Request_update_product,Request_delete_product
from models.sales import Request_new_sale, RequestCartById
from repositories.sales_repo import get_all_sales, get_sales_by_id
from service.sales_service import service_create_sale,service_update_sale,service_get_carts_by_id  
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# admin receber todos os usuários
@app.get("/")
def get_users():
    all_users = get_all_users()
    return all_users

@app.post("/auth")
def search_user(user:UserRequestLogin):
    response_login = verify_password(user.email,user.password) 

    return response_login

@app.post("/user/delete")
def delete_user(user:UserDeleteRequest):

    response = service_delete_user(user.user_id, user.authorization)

    return response 
    

# Qualquer pessoa criar novo usuário
@app.post("/create-user")
def create(user:UserCreateRequest):

    response = service_create_user(user.email, user.password, user.name)


    return response

#Pegar todos os produtos
@app.get("/products")
def receive_product():

    response_products = get_all_products()
    
    return response_products

@app.get("/products/{id}/image")
def receive_product_image(id:str):
    
    response = get_image_by_id(id)

    return Response(content=response)

@app.get("/products/{id}")
def receive_one_product(id:str):

    response = get_one_product(id)

    return response

# Criar novo produto
@app.post("/products")
async def create_product(
    name: str = Form(...),
    price: float = Form(...),
    authorization: str = Form(...),
    image: UploadFile = File(...)
    ):
    image_bytes = await image.read()
    response = service_create_product(price,name,image_bytes,authorization)

    return Response(content=response) 

@app.put("/product")
async def update_product( name: str = Form(None),
                   status:str = Form(None),
                   product_id:str = Form(None),
                   price: float = Form(None),
    authorization: str = Form(None),
    image: UploadFile = File(None)
        ):
    image_bytes = None 

    if image:
        image_bytes = await image.read()
    

    response = service_update_product(price,name,image_bytes,status,product_id,authorization)

    return response
    
@app.post("/product/delete")
def delete_product(product:Request_delete_product):

   response = service_delete_product(product.product_id, product.authorization)

   return response 

@app.post("/carts")
def get_carts_by_user_id(requisition:RequestCartById):
    
    response = service_get_carts_by_id(requisition.authorization)

    return response


@app.get("/sales")
def receive_sales():
    
    sales = get_all_sales()

    return sales

@app.get("/sales/{user_id}")
def get_one_sale_by_user_id(user_id:str):

    response = get_sales_by_id(user_id)
    
    return response

@app.post("/sales")
def new_sale(sale:Request_new_sale):

    response = service_create_sale(sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status, sale.authorization) 

    return response
    
@app.put("/sales")
def update_sale(sale:Request_new_sale):
  
    response = service_update_sale(sale.authorization,sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status) 


    return  response 

