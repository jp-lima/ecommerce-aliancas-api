from typing import reveal_type
from db import get_conn
from routes import products

def get_all_sales():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sales")
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

    cursor.execute("SELECT * FROM sales WHERE user_id = %s", (uuid,))
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales

def create_new_sale(uuid:str,user_id:str,product_id:str, amount:int,value:float, user_cep:str, status:str, code:str, sizes:str,state:str, city:str, neighboor:str,street:str, complement:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute(    '''
    INSERT INTO sales 
        (id,user_id, product_id, amount,value, user_cep,state, city, neighboor,street, complement, status, code, sizes )
    VALUES 
        (%s,%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s, %s, %s)
    ''',
    (uuid,user_id, product_id, amount,value, user_cep,state, city, neighboor,street, complement,status, code, sizes,)


 )

    conn.commit()

    cursor.close()
    conn.close()

def put_sale( amount:int,value:float, user_cep:str,status:str, uuid:str, code:str, sizes:str, state:str, city:str,neighboor:str,street:str, complement:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE sales SET 
        amount = %s,
        value = %s,
        user_cep = %s,
        status = %s,
        code = %s,
        sizes = %s,
        state = %s,
        city = %s,
        neighboor = %s,
        street = %s,
        complement = %s
    WHERE id = %s 
    ''',
    ( amount,value, user_cep,status, code, sizes,state, city,neighboor, street, complement,uuid)
 )

    conn.commit()

    cursor.close() 
    conn.close()

def get_sale_by_uuid(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `sales` WHERE id=%s",(uuid,))
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales













    
