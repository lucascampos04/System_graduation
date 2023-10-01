from Model.database import connect_database

def contratar_funcionarios(nome, telefone, cargo, salario):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO CONTRATAR_FUNCIONARIO(NOME, TELEFONE, FUNCAO, SALARIO) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome, telefone, cargo, salario))
            conn.commit()
            contratar_funcionario_id = cursor.lastrowid
            cursor.close()
            conn.close()
            print("Insert com sucesso")
            return contratar_funcionario_id
        except Exception as err:
            print(f"Erro ao inserir no banco de dados: {str(err)}")
