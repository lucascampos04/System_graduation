from Model.database import connect_database

def insert_registrar_buffet(nome, cnpj, endereco, tempoParceria, tipoParceria, email):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO CADASTRAR_BUFFETS(NOME, CNPJ, ENDERECO, TEMPO_DE_PARCERIA, TIPO_DE_BUFFETS, EMAIL) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nome, cnpj, endereco, tempoParceria, tipoParceria, email))
            conn.commit()
            contratar_funcionario_id = cursor.lastrowid
            cursor.close()
            conn.close()
            print("Insert com sucesso")
            return contratar_funcionario_id
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")

