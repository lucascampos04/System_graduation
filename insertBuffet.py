from database_connect import connect_database, close_database


# INSERT NOME
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
            print(f"Erro ao inserir no banco de dados: {str(err)}")

# INSERT CNPJ
def insert_cnpj_buffet(cnpj):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO cadastrar_buffet(cnpj) values (%s)"
            cursor.execute(query, (cnpj, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Foi kraiiiii")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

# INSERT EMMAIL
def insert_email_buffet(email):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO cadastrar_buffet(email) values (%s)"
            cursor.execute(query, (email, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Foi kraiiiii")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")