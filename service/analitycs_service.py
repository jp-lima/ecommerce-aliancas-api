from repositories.analitycs_repo import get_rows_of_analitycs, create_row_of_analitycs, put_row_of_analityc 
from repositories.analitycs_users_activity import get_all_rows_from_analitycs_users, create_row_analitycs_users, put_row_from_analitycs_users  
from routes import analitycs
from datetime import datetime
import locale
from datetime import datetime

def service_add_new_estatistic_on_analitycs(dict:dict):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    mes = datetime.now().strftime('%B')
    ano = datetime.now().year

    analitycs = get_rows_of_analitycs()

    data = {"revenue":analitycs[-1]["revenue"], "new_users": analitycs[-1]["new_users"], "orders_count":analitycs[-1]["orders_count"]}

    if analitycs[-1]["mounth"] == mes:

        match dict["estatistic"]:

            case "new_user":
                data["new_users"] += 1
            case "revenue":
                data["revenue"] += dict["data"] 
            case "orders_count":
                data["orders_count"] += 1 

        put_row_of_analityc(ano,mes, data["orders_count"], data["revenue"], data["new_users"] )

    else:

        create_row_of_analitycs(ano,mes, 0, 0 , 0  )

        service_add_new_estatistic_on_analitycs(dict) 

def service_post_a_user_online(command:str):

    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    #dt com ano passado para nunca ser igual a now caso lista all_rows seja vazia
    dt = datetime(2025, 1, 16, 10, 30, 0) 

    dict = {"users_online":0, "sales_mades":0,"datetime":dt, "new_users":0}

    all_rows = get_all_rows_from_analitycs_users()

    if all_rows:
        dict = all_rows[-1]
         
    match command:
            case "users_online":
                dict["users_online"] += 1 
            case "new_user":
                dict["new_users"] += 1
            case "sales_mades":
                dict["sales_mades"] += 1 


    now = datetime.now()
    # data + hora 
    if dict["datetime"].replace(minute=0,second=0, microsecond=0) == now.replace(minute=0, second=0, microsecond=0):
        put_row_from_analitycs_users(dict["users_online"] ,dict["sales_mades"], dict["datetime"],dict["new_users"] )
        print(dict) 
    # nada igual
    else:
        create_row_analitycs_users(now,dict["users_online"] ,dict["sales_mades"], dict["new_users"]) 

    return



