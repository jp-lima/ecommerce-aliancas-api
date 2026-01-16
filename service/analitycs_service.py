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

def service_post_a_user_online():

    #dt com ano passado para nunca ser igual a now caso lista all_rows seja vazia
    dt = datetime(2025, 1, 16, 10, 30, 0) 

    all_rows = get_all_rows_from_analitycs_users()

    if all_rows:
        dt = all_rows[-1]["datetime"]

    now = datetime.now()


    # data + hora 
    if dt.replace(minute=0,second=0, microsecond=0) == now.replace(minute=0, second=0, microsecond=0):
        put_row_from_analitycs_users(all_rows[-1]["users_online"] + 1, all_rows[-1]["sales_mades"], all_rows[-1]["datetime"])

    # nada igual
    else:
        create_row_analitycs_users(now, 1, 0) 

    return
