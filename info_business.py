from tkinter import Button, Frame, Tk, messagebox, Label, simpledialog, filedialog
import mysql.connector

'''colors'''
whitesmoke = "#dcdee8"
whiteBg = "#e6e7eb"
blackLight = "#3d3f47"
blackButLight = "#585959"
blue = "#213ac4"

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="senha123456",
            database="system_graduation"
        )
        return connection
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return None

def close_database(connection):
    if connection:
        connection.close()

# Função para obter o nome da empresa do banco de dados
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
    
def window_info_business(id):
    business_name = get_name(id)

    window = Tk()
    window.title("Informações da empresa")
    window.resizable(False, False)
    window.geometry("250x400")


    '''FRAMES'''
    frame_top = Frame(window, width=250, height=150, bg=blue)
    frame_top.grid(row=0, column=9)


    '''LABEL'''
    business_name = get_name(id)
    name_business = Label(frame_top, text=business_name)
    name_business.place(x=1)



    window.mainloop()


window_info_business(1)