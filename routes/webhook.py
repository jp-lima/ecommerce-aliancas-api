from models.webhook import * 
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException
from service.webhook_service import service_create_sale_by_webhook
import mercadopago
from service.sales_service import *

sdk = mercadopago.SDK("APP_USR-5708610925833516-012616-c46ac0af8146c4691ebc95ccf0d74968-443898421")

router = APIRouter(
prefix="/webhook",
tags=["webhook-yampi"]
        )

@router.post("/yampi")
async def receive_post(payload: WebhookYampi):


    service_create_sale_by_webhook(payload)

    return {"ok": True}
    
@router.post("/mercadopago")
def webhook(data: dict):
    payment_id = data.get("data", {}).get("id")

    payment = sdk.payment().get(payment_id)

    print(payment)
    if payment.get("response"):

        service_create_sale_by_webhook(payment["response"]["external_reference"])





