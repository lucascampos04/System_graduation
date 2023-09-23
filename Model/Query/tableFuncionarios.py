from Model.database import connect_database

def verificar_login(usuario, senha):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT matricula, usuario FROM logsFuncionarios WHERE usuario = %s AND senha = %s"
            cursor.execute(query, (usuario, senha))
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
