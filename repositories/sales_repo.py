from typing import reveal_type
from db import get_conn

def get_all_sales():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,user_id, product_id, amount,value, user_cep,status,created_at  FROM sales")
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales

def get_carts_by_id(uuid:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute("SELECT * FROM sales WHERE user_id = %s AND status = 'cart' ", (uuid,))

    carts = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return carts 
    

def get_sales_by_id(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,user_id, product_id, amount,value, user_cep,status,created_at  FROM sales WHERE user_id = %s", (uuid,))
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

def put_sale(user_id:str, product_id:str, amount:int,value:float, user_cep:str,status:str, uuid:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE sales SET 
        user_id = %s,
        product_id = %s,
        amount = %s,
        value = %s,
        user_cep = %s,
        status = %s
    WHERE id = %s 
    ''',
    (user_id, product_id, amount,value, user_cep,status, uuid)
 )

    conn.commit()

    cursor.close()
    conn.close()

def get_line_by_uuid(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `sales` WHERE id=%s",(uuid,))
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales













    
