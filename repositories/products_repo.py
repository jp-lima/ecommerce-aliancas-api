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






if __name__ == "__main__":
    user = get_all_products()

    print(user)



