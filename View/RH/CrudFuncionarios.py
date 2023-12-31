from tkinter import Tk, Label, Button, Entry, messagebox, ttk
from Components.Frames import *
from contratar_funcionario import windowFuncionarioADD
from Model.Query.tableFuncionarios import listar_funcionarios

global tabela_funcionarios
def preencher_tabela():
    registros = listar_funcionarios()

    for linha in tabela_funcionarios.get_children():
        tabela_funcionarios.delete(linha)

    for registro in registros:
        tabela_funcionarios.insert("", "end", values=registro)


def window_contratar_funcionario():
    windowFuncionarioADD()

def CrudFuncionarios():
    global tabela_funcionarios
    window = Tk()
    window.title("Funcionarios");
    window.geometry("500x500")

    frameT = frame_top(window, 500, 100, "white")
    frameT.grid(row=0, column=0)

    frameM = frame_meio(window, 500, 300, "white")
    frameM.grid(row=1, column=0)

    # Labels/Buttons
    btn_cre = Button(frameT, text="Contratar funcionario", font=("Arial 15 bold"), bg='white', fg='black', relief='flat', command=window_contratar_funcionario)
    btn_cre.place(x=30, y=30)

    btn_rmv = Button(frameT, text="Demitir funcionario", font=("Arial 15 bold"), bg='white', fg='black',relief='flat')
    btn_rmv.place(x=270, y=30)

    label_func = Label(frameM, text="Funcionarios", font=("Arial 25 bold"), bg='white', fg='black', relief='flat')
    label_func.place(x=130, y=10)

    # Tabela
    tabela_funcionarios = ttk.Treeview(frameM, columns=("Matricula", "Nome", "Salario", "Cargo"), show="headings")
    tabela_funcionarios.heading('#1', text="Matricula", anchor='center')
    tabela_funcionarios.heading('#2', text="Nome", anchor='center')
    tabela_funcionarios.heading('#3', text="Salario", anchor='center')
    tabela_funcionarios.heading('#4', text="Cargo", anchor='center')

    # Ajustar a largura das colunas
    tabela_funcionarios.column('#1', width=100, anchor='center')
    tabela_funcionarios.column('#2', width=100, anchor='center')
    tabela_funcionarios.column('#3', width=100, anchor='center')
    tabela_funcionarios.column('#4', width=120, anchor='center')

    style = ttk.Style()
    style.configure("Treeview.Heading", borderwidth=1, relief="solid", foreground="black")

    tabela_funcionarios.place(x=30, y=50)
    preencher_tabela()
    window.mainloop()

CrudFuncionarios()