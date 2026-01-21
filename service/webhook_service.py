from repositories.sales_repo import create_new_sale, get_sales_status_waiting_payment,put_sale  
from models.webhook import Merchant, CustomerInfos, ShippingAdress
from repositories.user_repo import get_all_users
from service.analitycs_service import service_add_new_estatistic_on_analitycs, service_post_a_user_online
from service.sales_service import service_update_sale 
from service.product_service import service_update_sales_of_product


def service_create_sale_by_webhook(payload:dict):

    
    ShippingAdress = payload.resource["shipping_address"]["data"]
    
    if payload.event == "order.paid":

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
        
                service_update_sales_of_product( 1, sale["product_id"])
                service_update_sale("admin",sale["id"],None, None, ShippingAdress["zipcode"], "pagamento confirmado", None,None,None,ShippingAdress["city"],ShippingAdress["neighborhood"], ShippingAdress["street"],ShippingAdress["complement"])  
                service_add_new_estatistic_on_analitycs({"estatistic":"revenue", "data": payload.resource["value_total"]})
                service_add_new_estatistic_on_analitycs({"estatistic":"orders_count", "data":""}) 
                service_post_a_user_online("sales_mades")
                break

    return
