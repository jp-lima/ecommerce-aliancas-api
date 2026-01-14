from repositories.analitycs_repo import get_rows_of_analitycs, create_row_of_analitycs, put_row_of_analityc 
from routes import analitycs
from datetime import datetime
import locale


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




