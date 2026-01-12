from fastapi import APIRouter
from repositories.analitycs_repo import create_row_of_analitycs, get_rows_of_analitycs    


router = APIRouter(

prefix = "/analitycs",
tags=["analitycs"]


)


@router.get("/")
def send_analitycs_by_mounth():

    response = get_rows_of_analitycs()

    return response











