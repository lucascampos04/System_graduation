from database_connect import close_database, connect_database
import mysql.connector

def inserir_name_school(name_faculdade):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(nome_da_faculdade) values (%s)"
            cursor.execute(query, (name_faculdade,))
            connection.commit()
            cursor.close()
            connection.close()
            print("Nome da faculdade inserio com sucesso")
        except Exception as err:
             print(f"Erro ao inserir no banco de dados: {str(err)}")

def inserir_name_curse(name_curso):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(nome_do_curso) values (%s)"
            cursor.execute(query, (name_curso, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Nome do curso inserio com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

def inserir_select_date(dates_select):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(data_disponiveis) VALUES(%s)"
            cursor.execute(query, (dates_select, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Data inserida com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

