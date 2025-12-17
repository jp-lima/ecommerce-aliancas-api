
from fastapi import APIRouter,Form,File, UploadFile,Response
from repositories.sales_repo import get_all_sales, get_sales_by_id
from service.sales_service import service_create_sale,service_update_sale,service_get_carts_by_id  

from models.sales import Request_new_sale, RequestCartById


router = APIRouter(

prefix ="/sales",
tags=["sales"]
        )


@router.post("/carts")
def get_carts_by_user_id(requisition:RequestCartById):
    
    response = service_get_carts_by_id(requisition.authorization)

    return response





@router.get("/")
def receive_sales():
    
    sales = get_all_sales()

    return sales

@router.get("/{user_id}")
def get_one_sale_by_user_id(user_id:str):

    response = get_sales_by_id(user_id)
    
    return response

@router.post("/")
def new_sale(sale:Request_new_sale):

    response = service_create_sale(sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status, sale.authorization) 

    return response
    
@router.put("/")
def update_sale(sale:Request_new_sale):
  
    response = service_update_sale(sale.authorization,sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status) 


    return  response 












