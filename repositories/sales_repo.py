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

def get_sales_status_waiting_payment():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sales WHERE status = 'aguardando pagamento'")
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales


def delete_sale_by_id(sale_id:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    DELETE FROM sales 
    WHERE id = %s 
    ''',
    (sale_id,)
 )

    conn.commit()

    cursor.close()
    conn.close()

    return


def get_carts_by_id(uuid:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute("SELECT * FROM sales WHERE user_id = %s AND status = 'cart' ", (uuid,))

    carts = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return carts 

def get_sale_by_sale_id(uuid:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute("SELECT * FROM sales WHERE id = %s ", (uuid,))

    sales = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return sales 

 

def get_sales_by_id(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sales WHERE user_id = %s", (uuid,))
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales

def create_new_sale(uuid:str,user_id:str,products_id:str, value:float, user_cep:str, status:str,state:str, city:str, neighboor:str,street:str, complement:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary = True)

    cursor.execute(    '''
    INSERT INTO sales 
        (id,user_id, products_id, value, user_cep,state, city, neighboor,street, complement, status )
    VALUES 
        (%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s)
    ''',
    (uuid,user_id, products_id, value, user_cep,state, city, neighboor,street, complement,status,)
 )

    conn.commit()

    cursor.close()
    conn.close()

def create_new_cart(uuid:str, user_id:str, products_id:dict):
    conn = get_conn()
    cursor = conn.cursor(dictionary = True)

    cursor.execute(    '''
    INSERT INTO sales 
        (id,user_id, products_id, status )
    VALUES 
        (%s, %s, %s, %s)
    ''',
    (uuid,user_id, products_id, 'cart' )
 )

    conn.commit()

    cursor.close()
    conn.close()

def put_an_cart(products_id:dict, uuid:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE sales SET 
        products_id = %s
    WHERE user_id = %s 
    ''',
    (products_id, uuid,)
 )

    conn.commit()

    cursor.close() 
    conn.close()





def put_json_sale( json:dict, uuid:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE sales SET 
        products_id = %s
    WHERE id = %s 
    ''',
    ( json,uuid)
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


def get_all_carts():

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `sales` WHERE status = 'cart'")
    sales = cursor.fetchall()

    cursor.close()
    conn.close()

    return sales


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










    
