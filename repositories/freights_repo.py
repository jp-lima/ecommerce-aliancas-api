from db import get_conn


def get_freights_data():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM freight")
    freights = cursor.fetchall()

    cursor.close()
    conn.close()

    return freights


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

def get_row_of_freight_by_city(city:str, state:str):

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM freight WHERE city = %s AND state = %s", (city,state,))
    freights = cursor.fetchall()

    cursor.close()
    conn.close()

    return freights


def get_row_of_freight_by_state(state:str):

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM freight WHERE state = %s AND city = ''", (state,))
    freights = cursor.fetchall()

    cursor.close()
    conn.close()

    return freights





