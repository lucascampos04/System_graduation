from tkinter import Tk, Label, Button, Entry, messagebox, ttk
from Model.database import connect_database, close_database
from Components.Frames import *
from Model.Query.funcionariosCrud import contratar_funcionarios

global entry_nome, \
    entry_telefone, \
    options_funcao, \
    funcao, \
    label_salario_trocar, \
    select_funcao, \
    label_salario, \
    label_cargo, \
    label_nome, \
    label_telefone, \
    select_name,\
    select_telefone, \
    label_nome, \
    entry_telefone, \
    label_telefone, \
    salario, \
    label_matricula

def on_funcao_selected(event):
    global funcao, select_funcao, label_cargo

    select_funcao = options_funcao.get()
    if select_funcao and select_funcao in funcao[:7]:
        label_salario_trocar.config(text="5.000,00")
        label_salario.config(text="5.000,00")
        label_cargo.config(text=select_funcao)

    elif select_funcao and select_funcao in funcao[8:]:
        label_salario_trocar.config(text="2.000,00")
        label_salario.config(text="2.000,00")
        label_cargo.config(text=select_funcao)
    else:
        label_salario_trocar.config(text="XXXXX")

def troca_dados():
    global select_name,select_telefone, label_nome, entry_telefone, label_telefone, select_funcao, label_matricula

    select_name = entry_nome.get()
    select_telefone = entry_telefone.get()
    label_nome.config(text=select_name)
    label_telefone.config(text=select_telefone)
    select_funcao = options_funcao.get()
    salario = 0;

    if select_funcao and select_funcao in funcao[:7]:
        salario = 5000
        funcionario_id = contratar_funcionarios(select_name, select_telefone, select_funcao, salario)
        label_matricula.config(text=funcionario_id)
        messagebox.showinfo("Sucesso", "Funcionario contratado com sucesso")
    elif select_funcao and select_funcao in funcao[8:]:
        salario = 2000
        funcionario_id = contratar_funcionarios(select_name, select_telefone, select_funcao, salario)
        label_matricula.config(text=funcionario_id)
        messagebox.showinfo("Sucesso", "Funcionario contratado com sucesso")

def windowFuncionarioADD():
    global entry_nome,\
        entry_telefone,\
        options_funcao,\
        funcao,\
        label_salario_trocar,\
        label_salario,\
        label_cargo,\
        label_nome,\
        label_telefone, \
        label_matricula

    window = Tk()
    window.title("Contratar funcionario")
    window.geometry("1200x500")
    window.resizable(False, False)

    frameT = frame_top(window, 700, 500, "blue")
    frameT.grid(row=0, column=0)

    frameT2 = frame_top(window, 500, 500, "white")
    frameT2.grid(row=0, column=1)


    # label e button contratando funcionario
    label_nome = Label(frameT, text="Nome: ", font=("Arial 15 bold"), bg="blue", fg="white")
    label_nome.place(x=30, y=50)
    entry_nome = Entry(frameT, width=20, font=("Arial 15 bold"))
    entry_nome.place(x=100, y=50)

    label_telefone = Label(frameT, text="Telefone: ", font=("Arial 15 bold"), bg="blue", fg="white")
    label_telefone.place(x=30, y=100)
    entry_telefone = Entry(frameT, width=20, font=("Arial 15 bold"))
    entry_telefone.place(x=130, y=100)

    # Data
    funcao = [
        "Chefe de cozinha",
        "Mestre de Cerimônias",
        "Coordenador de Eventos",
        "Gerente de Eventos",
        "Consultor de Casamentos",
        "Organizador de Festas",
        "Planejador de Eventos Corporativos",
        "Decorador de Eventos",
        "Florista de Eventos",
        "Fotógrafo de Eventos",
        "Videógrafo de Eventos",
        "DJ ou DJ de Casamentos",
        "Designer de Convites",
        "Maquiador e Cabeleireiro de Noivas",
        "Técnico de Iluminação e Som",
        "Garçom",
        "Segurança de Eventos"
    ]

    label_funcao = Label(frameT, text="Cargo : ", font=("Arial 15 bold"), bg='blue', fg="white")
    label_funcao.place(x=30, y=150)

    options_funcao = ttk.Combobox(frameT, values=funcao)
    options_funcao.place(x=130, y=150)
    options_funcao.bind("<<ComboboxSelected>>", on_funcao_selected)

    label_salario = Label(frameT, text="Salario : ", font=("Arial 15 bold"), bg='blue', fg="white")
    label_salario.place(x=30, y=200)

    label_salario_trocar = Label(frameT, text="XXXXX", font=("Arial 15 bold"), bg='blue', fg="white")
    label_salario_trocar.place(x=100, y=200)

    btn_contratar = Button(frameT, text="Contratar", font=("Arial 15 bold"), bg='black', fg="white", width=30, command=troca_dados)
    btn_contratar.place(x=50, y=300)

    # ficha de funncionario contratado
    title = Label(frameT2, text="FICHA FUNCIONARIO", width=50, bg="black", fg="white")
    title.place(x=80, y=50)

    label_matricula = Label(frameT2, text="Matricula : ", font=("Arial 15 bold"), fg="black")
    label_matricula.place(x=30, y=90)
    label_matricula = Label(frameT2, text="XXXXXXX", font=("Arial 15 bold"), fg="black")
    label_matricula.place(x=150, y=90)

    label_nome = Label(frameT2, text="Nome : ", font=("Arial 15 bold"), fg="black")
    label_nome.place(x=30, y=120)
    label_nome = Label(frameT2, text="XXXXXXX", font=("Arial 15 bold"), fg="black")
    label_nome.place(x=150, y=120)

    label_telefone = Label(frameT2, text="Telefone : ", font=("Arial 15 bold"), fg="black")
    label_telefone.place(x=30, y=150)
    label_telefone = Label(frameT2, text="XXXXXXX", font=("Arial 15 bold"), fg="black")
    label_telefone.place(x=150, y=150)

    label_cargo = Label(frameT2, text="Cargo : ", font=("Arial 15 bold"), fg="black")
    label_cargo.place(x=30, y=180)
    label_cargo = Label(frameT2, text="XXXXXXX", font=("Arial 15 bold"), fg="black")
    label_cargo.place(x=150, y=180)

    label_salario = Label(frameT2, text="Salario : ", font=("Arial 15 bold"), fg="black")
    label_salario.place(x=30, y=210)
    label_salario = Label(frameT2, text="XXXXXXX", font=("Arial 15 bold"), fg="black")
    label_salario.place(x=150, y=210)


    window.mainloop()
