from db import get_conn

def get_all_products():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,name,price,sales,type,material,stone, checkout_link, status, created_at FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

def get_one_product(product_id:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,name,sales,price,type,material,stone, checkout_link, status, created_at  FROM products WHERE id = %s",(product_id,))
    product = cursor.fetchall()

    cursor.close()
    conn.close()

    return product


def get_image_by_id(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT image_binary, image2_binary, image3_binary, image4_binary FROM products WHERE id = %s",(uuid,))
    images = cursor.fetchall()

    cursor.close()
    conn.close()
    
    i = list(images[0].values()) 

    return i 

def create_product(uuid:str, name:str, price:float, image_url:str, image_binary:str,image2_binary:str,image3_binary:str,image4_binary:str, type:str, stone:int, material:str,checkout_link:str, created_at:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO products 
        (id, name, price,image_binary,image2_binary,image3_binary,image4_binary,type, stone,material,checkout_link, created_at, updated_at, image_url)
    VALUES 
        (%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s,%s, %s)
    ''',
    (uuid, name,price,image_binary,image2_binary,image3_binary,image4_binary,type,stone, material,checkout_link,created_at,created_at, image_url)
    )

    conn.commit()

    cursor.close()
    conn.close()

def put_sale_of_one_product(sale:int, product_id:str):

    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE products SET 
        sales = %s
    WHERE id = %s 
    ''',
    (sale, product_id)
 )

    conn.commit()

    cursor.close()
    conn.close()


def put_product(name:str, price:float,updated_at:str,image_binary:str,image2_binary:str,image3_binary:str,image4_binary:str, status:str,type:str,material:str,checkout_link:str,uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE products SET 
        name = %s,
        price = %s,
        updated_at = %s,
        image_binary = %s,
        image2_binary = %s,
        image3_binary = %s,
        image4_binary = %s,
        status = %s,
        type= %s,
        material = %s,
        checkout_link = %s
    WHERE id = %s 
    ''',
    (name, price, updated_at,image_binary,image2_binary,image3_binary,image4_binary,status,type,material,checkout_link, uuid)
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
    get_image_by_id("fec99e9e-e60c-46d8-bd33-48cc77614a4a")



