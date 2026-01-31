from fastapi import APIRouter, Header
from models.freight_models import Request_Create_Freight
from service.freights_service import *
from service.freights_service import service_create_freight
from models.freight_models import *
from service.freights_service import service_delete_row_freight

router = APIRouter(
prefix="/freight",
tags=["freight"]
        )


@router.get("/")
async def get_freights(authorization: str = Header(None)):

    response = service_get_freights(authorization) 


    return response 

@router.post("/")
async def create_new_freight(request:Request_Create_Freight):

    response = service_create_freight(request) 

    return response

@router.delete("/{freight_id}")
async def dele_row_freight(freight_id:str,authorization: str = Header(None) ):

        
    response = service_delete_row_freight(authorization, freight_id)
    return response

@router.post("/calculate")
def calculate_freight(data:dict):

    response =  service_calculate_freight( data["state"], data["city"])
    
    return response


