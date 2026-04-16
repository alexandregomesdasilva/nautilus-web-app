import mysql.connector

def get_db_connection():
    # Retourne une connexion MySQL à la base de données "nautilus"
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="nautilus"
    )
    return connexion