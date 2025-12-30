from models.webhook import WebhookYampi
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException



router = APIRouter(
prefix="/webhook",
tags=["webhook-yampi"]
        )

@router.post("/yampi")
async def receive_post(payload: WebhookYampi):


    print(payload)

    return {"ok": True}
    





