from fastapi import FastAPI, UploadFile, File, Form,Response 


from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user, service_delete_user
from models.user import UserRequestLogin, UserCreateRequest, UserDeleteRequest    

from fastapi.middleware.cors import CORSMiddleware
from routes.sales import router as sales_router
from routes.users import router as users_router
from routes.products import router as products_router
from routes.webhook import router as webhook_yampi



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.includes_router(webhook_yampi)
app.include_router(users_router)
app.include_router(sales_router)

app.include_router(products_router)


