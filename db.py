import mysql.connector

def get_db_connection():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="nautilus"
    )
    return connexion