from db import get_conn

def get_all_sales():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,user_id, product_id, amount,value, user_cep,status,created_at  FROM sales")
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales

def create_new_sale(uuid:str,user_id:str,product_id:str, amount:int,value:float, user_cep:str, status:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute(    '''
    INSERT INTO sales 
        (id,user_id, product_id, amount,value, user_cep, status)
    VALUES 
        (%s,%s,%s,%s,%s,%s,%s)
    ''',
    (uuid,user_id, product_id, amount,value, user_cep,status)
 )

    conn.commit()

    cursor.close()
    conn.close()














    
