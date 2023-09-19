from model.database_connect import close_database, connect_database
import mysql.connector


'''Função para obter o nome da empresa do banco de dados'''
def get_name(id):
    try:
        connection = connect_database()
        if not connection:
            return "Erro ao conectar ao banco de dados"

        cursor = connection.cursor()
        cursor.execute('SELECT nome FROM dados_empresa WHERE id_empresa = %s', (id,))
        business_name = cursor.fetchone()
        cursor.close()
        close_database(connection)

        if business_name:
            return business_name[0]
        else:
            return "Empresa não encontrada"

    except mysql.connector.Error as err:
        print("Erro ao executar a consulta:", err)
        return "Erro ao executar a consulta"


'''Função para obter o email da empresa do banco de dados'''
def get_email(id):
    try:
        connection = connect_database()
        if not connection:
            return "Erro ao conectar ao banco de dados"

        cursor = connection.cursor()
        cursor.execute('SELECT email FROM dados_empresa WHERE id_empresa = %s', (id,))
        business_email = cursor.fetchone()
        cursor.close()
        close_database(connection)

        if business_email :
            return business_email[0]
        else:
            return "Empresa não encontrada"
    
    except mysql.connector.Error as err:
        print("Erro ao executar a consulta:", err)
        return "Erro ao executar a consulta"
    
'''Função para obter o telefone da empresa do banco de dados'''
def get_phone(id):
    try:
        connection = connect_database()
        if not connection:
            return "Erro ao conectar ao banco de dados"

        cursor = connection.cursor()
        cursor.execute('SELECT telefone FROM dados_empresa WHERE id_empresa = %s', (id,))
        business_email = cursor.fetchone()
        cursor.close()
        close_database(connection)

        if business_email :
            return business_email[0]
        else:
            return "Empresa não encontrada"
    
    except mysql.connector.Error as err:
        print("Erro ao executar a consulta:", err)
        return "Erro ao executar a consulta"
    
'''Função para obter o endereço da empresa do banco de dados'''
def get_ende(id):
    try:
        connection = connect_database()
        if not connection:
            return "Erro ao conectar ao banco de dados"

        cursor = connection.cursor()
        cursor.execute('SELECT endereco FROM dados_empresa WHERE id_empresa = %s', (id,))
        business_email = cursor.fetchone()
        cursor.close()
        close_database(connection)

        if business_email :
            return business_email[0]
        else:
            return "Empresa não encontrada"
    
    except mysql.connector.Error as err:
        print("Erro ao executar a consulta:", err)
        return "Erro ao executar a consulta"