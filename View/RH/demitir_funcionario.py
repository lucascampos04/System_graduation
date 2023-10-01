from tkinter import Tk, Label, Button, Entry, messagebox, ttk
from Model.database import connect_database, close_database
from Components.Frames import *
from Model.Query.funcionariosCrud import demitir_funcionario

global entry_matricula
def delete_funcionario():
    global entry_matricula
    matricula = entry_matricula.get()

    demitir_funcionario(matricula)

def windowDmeitir():
    global entry_matricula

    window = Tk()
    window.geometry("300x600")
    window.resizable(False, False)
    window.title("Demitir funcionario")

    frameT = frame_top(window, 300, 250, "white")
    frameT.grid(row=0, column=0)

    frameE = frame_final(window, 300, 350, "red")
    frameE.grid(row=1, column=0)

    title_window = Label(frameT, text="Demitir Funcionario", font=("Arial 20 bold"), bg="white")
    title_window.place(x=20, y=30)

    # Frame top
    label_matricula = Label(frameT, text="Matricula", font=("Arial 18 bold"))
    label_matricula.place(x=60, y=80)
    entry_matricula = Entry(frameT, font=("Arial 15 bold"))
    entry_matricula.place(x=20, y=120)

    btn_demitir = Button(frameT, text="Demitir", font=("Ivy 15 bold"), command=delete_funcionario)
    btn_demitir.place(x=80, y=150)

    # frame final

    window.mainloop()

windowDmeitir()