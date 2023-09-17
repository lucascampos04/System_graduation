from database_connect import close_database, connect_database

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


def inserir_endereco(adress, ponto_referencia):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(enderecos_disponiveis, ponto_de_referencia) VALUES(%s, %s)"
            cursor.execute(query, (adress, ponto_referencia))
            connection.commit()
            cursor.close()
            connection.close()
            print("Endereço e Ponto de referencia insirido com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

def inserir_duracao_prevista(duracao_prevista):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(horarios_disponiveis) VALUES(%s)"
            cursor.execute(query, (duracao_prevista, ))
            connection.commit()
            cursor.close()
            connection.close()
            print("Horario insirido com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

def inserir_tipo_evento(tipo_evento, limit_convidado):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO marca_evento(evento_aberto_ou_fechado, limite_de_convidados) VALUES(%s, %s)"
            cursor.execute(query, (tipo_evento, limit_convidado))
            connection.commit()
            cursor.close()
            connection.close()
            print("Tipo do Evento e Limite de convidados insiridos com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")
