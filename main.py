from repositories import products_repo
from fastapi import FastAPI
from db import get_conn
from pydantic import BaseModel 
from repositories.products_repo import get_all_products
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user  
from service.product_service import service_create_product, service_delete_product, service_update_product
from models.user import UserRequestLogin, UserCreateRequest   
from models.model_product import Request_create_product, Request_update_product,Request_delete_product
from models.sales import Request_new_sale 
from repositories.sales_repo import get_all_sales
from service.sales_service import service_create_sale,service_update_sale
from repositories.sales_repo import put_sale
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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


# Qualquer pessoa criar novo usuário
@app.post("/create-user")
def create(user:UserCreateRequest):

    response = service_create_user(user.email, user.password, user.name)


    return response

#Pegar todos os produtos
@app.get("/products")
def receve_product():

    response_products = get_all_products()
    
    return response_products

# Criar novo produto
@app.post("/products")
def create_product(product:Request_create_product):

    response = service_create_product(product.price, product.name, product.image_url, product.authorization)
    

    return response

@app.put("/product")
def update_product(product:Request_update_product):

    response = service_update_product(product.price, product.name, product.image_url,product.status,product.product_id, product.authorization)

    return response
    
@app.post("/product/delete")
def delete_product(product:Request_delete_product):

   response = service_delete_product(product.product_id, product.authorization)

   return response 


@app.get("/sales")
def receive_sales():
    
    sales = get_all_sales()

    return sales


@app.post("/sales")
def new_sale(sale:Request_new_sale):

    response = service_create_sale(sale.product_id, sale.amount,sale.value,sale.user_cep, sale.authorization) 

    return response
    
@app.put("/sales")
def update_sale(sale:Request_new_sale):
  
    response = service_update_sale(sale.authorization,sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status) 


    return  response 



