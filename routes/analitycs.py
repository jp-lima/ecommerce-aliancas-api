from fastapi import APIRouter
from repositories.analitycs_repo import create_row_of_analitycs, get_rows_of_analitycs, put_row_of_analityc   
from service.analitycs_service import service_add_new_estatistic_on_analitycs

router = APIRouter(

prefix = "/analitycs",
tags=["analitycs"]


)

# Criar usuário, compra paga, valor da compra


@router.get("/")
def send_analitycs_by_mounth():

    response = get_rows_of_analitycs()

    return response

@router.post("/user-loged")
def user_be_loged():

    return "running"



