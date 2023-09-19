from database_connect import connect_database, close_database



def insert_name_buffet(name):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO cadastrar_buffet(nome) values (%s)"
            cursor.execute(query, (name, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Foi kraiiiii")
        except Exception as err:
            print("Erro ao inserir no banco de dados ", err)