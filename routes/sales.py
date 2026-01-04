
from fastapi import APIRouter,Header,Form,File, UploadFile,Response
from repositories.sales_repo import get_all_sales, get_sales_by_id, get_sale_by_sale_id
from service.sales_service import service_create_sale,service_update_sale,service_get_carts_by_id, service_del_cart_by_id  

from models.sales import Request_new_sale, RequestCartById, Request_put_sale


router = APIRouter(

prefix ="/sales",
tags=["sales"]
        )


@router.post("/carts")
def get_carts_by_user_id(requisition:RequestCartById):
    
    response = service_get_carts_by_id(requisition.authorization)

    return response

@router.delete("/carts")
def delete_carts_by_user_id(Authorization: str = Header(None), cart_id:str = None):
    
    response = service_del_cart_by_id(Authorization, cart_id) 


    return response 


@router.get("/")
def receive_sales():
    
    sales = get_all_sales()

    return sales

@router.get("/{user_id}")
def get_one_sale_by_user_id(user_id:str):

    response = get_sales_by_id(user_id)
    
    return response

@router.get("/sale/{sale_id}")
def get_sale_by_id(sale_id:str):

    response = get_sale_by_sale_id(sale_id) 

    return response 

@router.post("/")
def new_sale(sale:Request_new_sale):

    response = service_create_sale(sale.product_id, sale.amount,sale.value,sale.user_cep, sale.status, sale.authorization, sale.code, sale.sizes, sale.state, sale.city, sale.neighboor, sale.street, sale.complement) 

    return sale 
    
@router.put("/")
def update_sale(sale:Request_put_sale):
  
    response = service_update_sale(sale.authorization,sale.sale_id, sale.amount,sale.value,sale.user_cep, sale.status, sale.code, sale.sizes,sale.state, sale.city, sale.neighboor, sale.street, sale.complement) 


    return  response 







