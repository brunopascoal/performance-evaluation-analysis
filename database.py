import pymysql
import pandas as pd

def create_connection():
    host = 'host_here'
    port = 3306
    user = "user_here"
    password = "password_here"
    database = "database_here"

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    return connection



def get_data(connection):
    query = """query_sql_here"""

    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [i[0] for i in cursor.description]
        results = cursor.fetchall()

    return pd.DataFrame(results, columns=columns)