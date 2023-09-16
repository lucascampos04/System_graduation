import random
from tkinter import messagebox, simpledialog, Tk, Frame, Label, Button, Entry, ttk
from tkcalendar import Calendar 

from insertDataSchoolRepository import inserir_name_school, inserir_name_curse, inserir_select_date

def number_random():
    number = random.choice(1000, 90000)

def inserir_nome_faculdade():
    nome_faculdade = simpledialog.askstring("Inserir nome", "Digite o nome da Faculdade")
    if nome_faculdade:
        inserir_name_school(nome_faculdade)
        button_inserir_nome_faculdade.config(text=nome_faculdade, font=("Arial 15 bold") ,command=None, relief='flat',bg="blue")

def inserir_nome_curso():
    nome_curso = simpledialog.askstring("Inserir", "Digite o nome do curso")
    if nome_curso:
        inserir_name_curse(nome_curso)
        button_inserir_nome_curso.config(text=nome_curso)

def selecionar_data(event):
    global data_selecionada
    data_selecionada = combo_date.get()
    inserir_select_date(data_selecionada)

    # remove a data selecionada do combos
    combo_date.set("")
    combo_date["values"] = [data for data in datas if data != data_selecionada]

    label_data_selecionada = Label(frame_midle, text=f"Data selecionada: {data_selecionada}", font=("Arial 14 bold"), bg="blue")
    label_data_selecionada.place(x=20, y=170)

    
    
    



def methhod_brand_graduation():
    window = Tk()
    window.title("Marca formatura")
    window.resizable(False, False)
    window.geometry("600x500")

    '''FRAMES'''
    global frame_midle
    frame_top = Frame(window, width=600, height=150, bg="black")
    frame_top.grid(row=0, column=0)

    frame_midle = Frame(window, width=600, height=350, bg="blue")
    frame_midle.grid(row=1, column=0)

    title_branda_graduation = Label(frame_top, text="MARQUE SUA FORMATURA", font=("Arial 16 bold"), bg="black", fg="white")
    title_branda_graduation.place(x=10, y=70)

    # Nome da faculdade 

    label_name_school = Label(frame_midle, text="Nome da Universidade", font=("Arial 14 bold"), bg="blue")
    label_name_school.place(x=20, y=25)

    global button_inserir_nome_faculdade
    button_inserir_nome_faculdade = Button(frame_midle, text="Clique aqui e digite o nome da Faculdade", command=inserir_nome_faculdade)
    button_inserir_nome_faculdade.place(x=20, y=60)

    # Nome do curso

    label_name_curse = Label(frame_midle, text="Nome da curso", font=("Arial 14 bold"), bg="blue")
    label_name_curse.place(x=300, y=25)

    global button_inserir_nome_curso
    button_inserir_nome_curso = Button(frame_midle, text="Clique aqui e digite o nome do curso", command=inserir_nome_curso)
    button_inserir_nome_curso.place(x=300, y=60)

    # Escolher uma data
    label_select_date = Label(frame_midle, text="Escolha uma data", font=("Arial 14 bold"), bg="blue")
    label_select_date.place(x=20, y=100)
    
    global datas
    datas = [
    "2023-01-15",
    "2023-03-10",
    "2023-05-05",
    "2023-06-20",
    "2023-08-12",
    "2023-09-04",
    "2023-10-17",
    "2023-12-01",
    "2023-02-25",
    "2023-04-14",
    "2023-07-08",
    "2023-11-22"
]
    global combo_date
    combo_date =  ttk.Combobox(frame_midle, values=datas)
    combo_date.place(x=20, y=140)
    combo_date.bind("<<ComboboxSelected>>", selecionar_data)


    


    window.mainloop()

methhod_brand_graduation()