from Model.database import connect_database

def verificar_login(matricula, nome):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT matricula, nome FROM CONTRATAR_FUNCIONARIO WHERE matricula = %s AND nome = %s"
            cursor.execute(query, (matricula, nome))
            resultado = cursor.fetchone()

            if resultado:
                matricula, nome = resultado
                print(f"Login bem-sucedido para o funcionário {nome} (Matrícula: {matricula})")
            else:
                print("Login falhou. Usuário ou senha incorretos.")

            cursor.close()
            conn.close()

        except Exception as err:
            print(f"Erro ao verificar o login: {str(err)}")



def listar_funcionarios():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT MATRICULA, NOME, SALARIO, FUNCAO FROM CONTRATAR_FUNCIONARIO"
            cursor.execute(query)
            funcionarios = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Consulta com sucesso")
            return funcionarios
        except Exception as err:
            print(f"Erro ao consultar o banco de dados: {str(err)}")

