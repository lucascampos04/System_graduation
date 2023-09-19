from Model.database import connect_database


# Insert tabela faculdade
def insertNameFaculdade(faculdade):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO FACULDADE(nome) values (%s)"
            cursor.execute(query, (faculdade,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")


# ----------------------------------------------------------------------------------- #

# Insert tabela curso
def insertNameCurso(curso):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO CURSO(curso) values (%s)"
            cursor.execute(query, (curso,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

# ----------------------------------------------------------------------------------- #

# Insert tabela evento
def insertNameEvento(evento):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO EVENTO(evento) values (%s)"
            cursor.execute(query, (evento,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")


# ----------------------------------------------------------------------------------- #

# Insert tabela status
def insertNameStatus(status):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO STATUS (status) values (%s)"
            cursor.execute(query, (status,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")


# ----------------------------------------------------------------------------------- #

# Insert tabela forma de pagamento
def insertNameForma(forma):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO FORM_PAGMENTO (forma) values (%s)"
            cursor.execute(query, (forma,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

# ----------------------------------------------------------------------------------- #

# insert tabela formatura
