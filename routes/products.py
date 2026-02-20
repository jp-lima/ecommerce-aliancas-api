from fastapi import APIRouter,Form,File, UploadFile,Response
from models.model_product import Request_create_product, Request_update_product,Request_delete_product
from repositories.products_repo import get_all_products, get_image_by_id, get_one_product
from service.product_service import *

router = APIRouter(
prefix="/products",
tags=["products"]
        )

@router.get("/teste")
async def teste():

    response =  await delete_image_from_supabase("https://qqxlznjxpekbpqblakju.supabase.co/storage/v1/object/public/products/PA27.png")

    return


@router.get("/")
def receive_product():

    response_products = get_all_products()
    
    return response_products


@router.get("/{id}/image/{index}")
def receive_product_image(id:str, index:int):
    
    #response = get_image_by_id(id)
    
    response = service_get_image_for_product(id, index)

    return Response(content=response) 

@router.get("/{id}")
def receive_one_product(id:str):

    response = get_one_product(id)

    return response

# Criar novo produto
@router.post("/")
async def create_product(
    name: str = Form(...),
    price: float = Form(...),
    authorization: str = Form(...),
    type: str = Form(...),
    material: str = Form(...),
    checkout_link: str = Form(...),
    stone: int = Form(...), 
    image: UploadFile = File(...),
    image2: UploadFile = File(None),
    image3: UploadFile = File(None),
    ):
    image_bytes = await image.read()
    
    image2_bytes = await image2.read() if image2 else "" 
    image3_bytes = await image3.read() if image3 else "" 
    
    response = await service_create_product(price,name,image_bytes,image2_bytes,
    image3_bytes,type,stone,material,checkout_link,authorization, image, image2, image3)

    return response

@router.put("/")
async def update_product( 
        name: str = Form(None),
        status:str = Form(None),
        authorization: str = Form(None),
        product_id:str = Form(None),
        price: float = Form(None),
        type: str = Form(None),
        material: str = Form(None),
        checkout_link: str = Form(None),
        image: UploadFile = File(None),
        image2: UploadFile = File(None),
        image3: UploadFile = File(None),
        image4: UploadFile = File(None)
                         ):
    image_bytes = None 

    image_bytes = await image.read() if image else "" 
    image2_bytes = await image2.read() if image2 else "" 
    image3_bytes = await image3.read() if image3 else "" 
    image4_bytes = await image4.read() if image4 else "" 


    response = await service_update_product(price,name,image,image2,image3,status,type,material,checkout_link,product_id,authorization)

    return response
    
@router.post("/delete")
def delete_product(product:Request_delete_product):

   response = service_delete_product(product.product_id, product.authorization)

   return response 

