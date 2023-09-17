from database_connect import close_database, connect_database

# nome de representante
def inserir_name_representante(name_representante):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO representante_de_classe(nome) VALUES (%s)"
            cursor.execute(query, (name_representante, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Nome de representante inserido com sucesso")
        except Exception as err:
             print(f"Erro ao inserir no banco de dados: {str(err)}")

# telefone de representante
def inserir_telefone_representante(telefone):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO representante_de_classe(telefone) VALUES (%s)"
            cursor.execute(query, (telefone, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("telefone de representante inserido com sucesso")
        except Exception as err:
             print(f"Erro ao inserir no banco de dados: {str(err)}")


# froma de pagamento de representante
def inserir_forma_de_pagamento_representante(forma_pagamento):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO representante_de_classe(forma_pag) VALUES (%s)"
            cursor.execute(query, (forma_pagamento, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Forma de pagamento inserido com sucesso")
        except Exception as err:
             print(f"Erro ao inserir no banco de dados: {str(err)}")

# email de pagamento de representante
def inserir_email_representante(email):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO representante_de_classe(email) VALUES (%s)"
            cursor.execute(query, (email, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Email inserido com sucesso")
        except Exception as err:
             print(f"Erro ao inserir no banco de dados: {str(err)}")
            