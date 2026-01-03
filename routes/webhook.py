from models.webhook import WebhookYampi
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException
from service.webhook_service import service_create_sale_by_webhook


router = APIRouter(
prefix="/webhook",
tags=["webhook-yampi"]
        )

@router.post("/yampi")
async def receive_post(payload: WebhookYampi):


    service_create_sale_by_webhook(payload)

    return {"ok": True}
    





