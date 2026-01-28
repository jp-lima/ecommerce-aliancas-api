
from db import get_conn



def get_freights_data():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM freight")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products


def create_row_freight(uuid:str,state:str, city:int, value:float):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
    '''
    INSERT INTO freight 
        (id,state, city, value)
    VALUES 
        (%s,%s,%s,%s)
    ''',
    (uuid,state, city, value,)
    )

    conn.commit()

    cursor.close()
    conn.close()

def del_row_freight(uuid:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    DELETE FROM freight 
    WHERE id = %s 
    ''',
    (uuid,)
 )

    conn.commit()

    cursor.close()
    conn.close()







