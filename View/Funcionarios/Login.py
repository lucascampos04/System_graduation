from tkinter import Tk, Label, Button, Entry, messagebox
from Components.Frames import *
from Model.Query.tableFuncionarios import verificar_login
global id_input, senha_input
from View.RH.contratar_funcionario import windowFuncionarioADD
def getUser(id_input):
    return id_input.get()
def getSenha(senha_input):
    return senha_input.get()
def entrar():
    user = getUser(id_input)
    senha = getSenha(senha_input)
    if user == "admin" and senha == "admin":
        windowFuncionarioADD()
        return True

    if verificar_login(user, senha):
        messagebox.showinfo("Login feito com sucesso", "Login realizado com sucesso")
    else:
        messagebox.showerror("Usuário ou senha inexistente", "Usuário ou senha inexistente")

def login_funcionario():
    global id_input, senha_input
    window = Tk()
    window.title("Tela inicial")
    window.geometry("300x400")
    window.resizable(False, False)

    # Frames
    frameT = frame_top(window, 300, 100, 'black')
    frameT.grid(row=0, column=0)

    frameM = frame_meio(window, 300, 350, 'white')
    frameM.grid(row=1, column=0)

    # frame top
    title_frame_top = Label(frameT, text="FUNCIONARIOS", font=("Arial 29 bold"), bg='black', fg='white')
    title_frame_top.place(x=1, y=20)

    # frame meio
    id_label = Label(frameM, text="Número de identificação", font=("Arial 13 bold"), bg="white")
    id_label.place(x=50, y=40)
    id_input = Entry(frameM, width=30)
    id_input.place(x=50, y=70)

    senha_label = Label(frameM, text="Senha", font=("Arial 13 bold"), bg="white")
    senha_label.place(x=50, y=120)
    senha_input = Entry(frameM, width=30)
    senha_input.place(x=50, y=150)

    # Botão
    btn_login = Button(frameM, text="Entrar",width=10, font=("Arial 15 bold"), command=entrar)
    btn_login.place(x=25, y=200)

    window.mainloop()

