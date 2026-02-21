from db import get_conn

def get_all_products():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,name,price,sales,type,image_url, image2_url, image3_url,  material,stone, solitary, pear, checkout_link, status, created_at FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

def get_one_product(product_id:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,name,sales,price,type,material,stone,solitary, pear, image_url, image2_url, image3_url, checkout_link, status, created_at  FROM products WHERE id = %s",(product_id,))
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

def create_product(uuid:str, name:str, price:float, image_url:str, image2_url:str, image3_url:str, type:str, stone:int, solitary:int, pear:int, material:str,checkout_link:str, created_at:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO products 
    (id, name, price,type, stone,solitary, pear,material,  checkout_link, created_at, updated_at, image_url, image2_url, image3_url)
    VALUES 
        (%s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)
    ''',
    (uuid, name,price,type,stone,solitary,pear , material,checkout_link,created_at,created_at, image_url, image2_url, image3_url)
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


def put_product(name:str, price:float,updated_at:str,image_url:str,image2_url:str,image3_url:str, status:str,type:str,stone:int, solitary:int, pear:int, material:str,checkout_link:str,uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    UPDATE products SET 
        name = %s,
        price = %s,
        updated_at = %s,
        image_url = %s,
        image2_url = %s,
        image3_url = %s,
        status = %s,
        type= %s,
        stone = %s,
        solitary = %s,
        pear = %s,
        material = %s,
        checkout_link = %s
    WHERE id = %s 
    ''',
    (name, price, updated_at,image_url,image2_url,image3_url,status,type,stone, solitary, pear,material,checkout_link, uuid)
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



