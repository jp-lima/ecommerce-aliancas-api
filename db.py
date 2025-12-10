from mysql.connector import pooling

db_pool = pooling.MySQLConnectionPool(
    pool_name = "aliancas",
    pool_size = 5,  
    host = "srv1922.hstgr.io",
    password="@Hebertmiguel1706",
    user="u670476727_hebert",
    database="u670476727_aliancas",
    port=3306
)

def get_conn():
    return db_pool.get_connection()

