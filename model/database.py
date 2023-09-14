import mysql.connection

def connect_database():
    try:
        bank = mysql.connection.connect(
            host="localhost", user="root", password="senha12345", database="system"
        )
    except mysql.connection.errors as err:
        print("Erro ao conectar no banco de dados", err)
        return None
