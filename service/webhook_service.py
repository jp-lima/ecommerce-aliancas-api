from repositories.sales_repo import create_new_sale, get_sales_status_waiting_payment,put_sale  
from models.webhook import Merchant, CustomerInfos
from repositories.user_repo import get_all_users

from service.sales_service import service_update_sale 

#uuid:str,user_id:str,product_id:str, amount:int,value:float, user_cep:str, status:str, code:str, sizes:str,state:str, city:str, neighboor:str,street:str, complement:str):

#saber id do produto pelo preço e id do usuário
#um produto deve ficar com status "aguardando pagamento" por uns 30 minutos

def service_create_sale_by_webhook(payload:dict):

#    print(payload)
    if payload.event == "order.paid":

#        Merchant = payload.merchant
        user_founded = {}    
        CustomerInfos = payload.resource["customer"]["data"]  
        
        customer_name = CustomerInfos["name"].lower().replace(" ", "")
        all_users = get_all_users()
        

        for user in all_users:

            user_name =  user["name"].lower().replace(" ", "")  

            if user_name in customer_name or customer_name in user_name:
                user_founded = user
                print(user_founded)

        sales = get_sales_status_waiting_payment()

        for sale in sales:

            if sale["value"] == payload.resource["value_total"] and len(user_founded.items()) > 0:
                print(sale)
                print("ENCONTRADO")
                
                service_update_sale("admin",sale["id"],None, None, None, "pagamento confirmado", None,None,None,None,None, None,None)  
       


    return
