from db import get_conn



def create_row_of_analitycs(year:str, mounth:str, orders_count:int, revenue:float, new_users:int):
    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO analitycs_by_mounth 
        (year, mounth, orders_count, revenue, new_users)
    VALUES 
        (%s,%s,%s,%s,%s)
    ''',
    (year,mounth ,orders_count, revenue, new_users )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_rows_of_analitycs():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM analitycs_by_mounth")
    datas = cursor.fetchall()

    cursor.close()
    conn.close()

    return datas






