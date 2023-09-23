from Model.database import connect_database

def insertFormatura(id_faculdae, id_curso,representante, id_formaP, total, tipo_form, lmt):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO FORMATURA (FACULDADE, CURSO, REPRESENTANTE, FORM_PAGAMENTO, TOTAL, TIPO_FORMATURA, LIMIT_PESSOAS) VALUES (%s, %s, %s, %s, %s, %s, %s) "
            cursor.execute(query, (id_faculdae, id_curso,representante, id_formaP, total, tipo_form, lmt))
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert com sucesso")
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")