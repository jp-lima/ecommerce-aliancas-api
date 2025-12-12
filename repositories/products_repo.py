from db import get_conn

def get_all_products():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,name,price,sales,created_at,updated_at,image_url,status  FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

def create_product(uuid:str, name:str, price:float,image_url:str, created_at:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO products 
        (id, name, price, image_url,created_at, updated_at)
    VALUES 
        (%s,%s,%s,%s,%s,%s)
    ''',
    (uuid, name,price,image_url,created_at,created_at)
    )

    conn.commit()

    cursor.close()
    conn.close()

def put_product(name:str, price:float,updated_at:str,image_binary:str, status:str,uuid:str):
    
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE products SET 
        name = %s,
        price = %s,
        updated_at = %s,
        image_binary = %s,
        status = %s
    WHERE id = %s 
    ''',
    (name, price, updated_at,image_binary,status, uuid)
 )

    conn.commit()

    cursor.close()
    conn.close()

def del_product(uuid:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    DELETE FROM products
    WHERE id = %s 
    ''',
    (uuid,)
 )

    conn.commit()

    cursor.close()
    conn.close()



if __name__ == "__main__":
    user = get_all_products()

    print(user)



