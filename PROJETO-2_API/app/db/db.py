import mysql.connector

def get_connection():
    return mysql.connector(
        host="localhost",
        user="root",
        password="2005",
        database="api",
    )
    
connection = get_connection()
cursor = connection.cursor(Dictionaty=True)