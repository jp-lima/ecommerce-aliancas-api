from fastapi import APIRouter,Form,File, UploadFile,Response
from models.model_product import Request_create_product, Request_update_product,Request_delete_product


from repositories.products_repo import get_all_products, get_image_by_id, get_one_product
from service.product_service import service_create_product, service_delete_product, service_update_product, service_update_sales_of_product


router = APIRouter(
prefix="/products",
tags=["products"]
        )

@router.get("/")
def receive_product():

    response_products = get_all_products()
    
    return response_products

@router.get("/teste")
def teste():
    service_update_sales_of_product(1,"2969ac0f-bc0d-4252-99d4-9dd6a258bb8e")

    return

@router.get("/{id}/image")
def receive_product_image(id:str):
    
    response = get_image_by_id(id)

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
    image4: UploadFile = File(None)
    ):
    image_bytes = await image.read()
    
    image2_bytes = await image2.read()
    image3_bytes = await image3.read()
    image4_bytes = await image4.read()
    
    response = service_create_product(price,name,image_bytes,image2_bytes, image3_bytes, image4_bytes,type,stone,material,checkout_link,authorization)

    return Response(content=response) 

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
        image: UploadFile = File(None)
        ):
    image_bytes = None 

    if image:
        image_bytes = await image.read()
    

    response = service_update_product(price,name,image_bytes,status,type,material,checkout_link,product_id,authorization)

    return response
    
@router.post("/delete")
def delete_product(product:Request_delete_product):

   response = service_delete_product(product.product_id, product.authorization)

   return response 

