import pymysql
import pandas as pd

def create_connection():
    host = ''
    port = 3306
    user = ""
    password = ""
    database = ""

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    return connection



def get_data(connection):
    query = """query"""
# Pesquisar sobre SQL Injection
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [i[0] for i in cursor.description]
        results = cursor.fetchall()

    return pd.DataFrame(results, columns=columns)