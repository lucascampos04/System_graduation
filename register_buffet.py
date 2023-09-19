from tkinter import Button, Frame, Tk, Label, Entry, ttk
from insertBuffet import insert_name_buffet, insert_cnpj_buffet

getNameEntry = None
getCnpjEntry = None

def setNameBuffet():
    global getNameEntry
    getNameEntry = entry_name_buffet.get()

def setCnpjBuffet():
    global getCnpjEntry
    getCnpjEntry = entry_cnpj_buffet.get()

def registrar():
    global getNameEntry, getCnpjEntry
    insert_name_buffet(getNameEntry)
    insert_cnpj_buffet(getCnpjEntry)

def buffet():
    global entry_name_buffet, entry_cnpj_buffet, entry_email_buffet, getNameEntry, getCnpjEntry
    window_register_buffet = Tk()
    window_register_buffet.title("Buffet")
    window_register_buffet.resizable(False, False)
    window_register_buffet.geometry("400x500")

    '''FRAMES'''
    frame_top = Frame(window_register_buffet, width=400, height=140, bg="black")
    frame_top.grid(column=0, row=0)

    frame_middle = Frame(window_register_buffet, width=400, height=420, bg="white")
    frame_middle.grid(row=1, column=0)

    '''FRAMES/BUTTONS'''

    # Nome
    name_buffet = Label(frame_middle, text="Nome : ", font=("Arial 13 bold"), bg="white")
    name_buffet.place(x=10, y=20)
    entry_name_buffet = Entry(frame_middle)
    entry_name_buffet.place(x=120, y=25)

    # Cnpj
    cnpj_buffet = Label(frame_middle, text="Cnpj : ", font=("Arial 13 bold"), bg="white")
    cnpj_buffet.place(x=10, y=60)
    entry_cnpj_buffet = Entry(frame_middle)
    entry_cnpj_buffet.place(x=120, y=65)

    # Endereço
    endereco_buffet = Label(frame_middle, text="Endereço : ", font=("Arial 13 bold"), bg="white")
    endereco_buffet.place(x=10, y=100)
    entry_endereco_buffet = Entry(frame_middle)
    entry_endereco_buffet.place(x=120, y=105)

    # tempo de parceria
    tempo_de_parceria = Label(frame_middle, text="Tempo de Parceira", font=("Arial 13 bold"), bg="white")
    tempo_de_parceria.place(x=10, y=140)

    tempo = [
        "1 Semestre",
        "2 Semestre",
        "3 Semestre",
        "4 Semestre",
    ]

    box_tempo_parceria = ttk.Combobox(frame_middle, values=tempo)
    box_tempo_parceria.place(x=170, y=145)
    box_tempo_parceria.bind("<<ComboboxSelected>>")

    # tipo de parceria
    tipo_de_parceria = Label(frame_middle, text="Tipo de Parceira", font=("Arial 13 bold"), bg="white")
    tipo_de_parceria.place(x=10, y=180)

    tipo_parceria = [
        "Associadp",
        "Parceiro",
    ]

    box_tipo_parceria = ttk.Combobox(frame_middle, values=tipo_parceria)
    box_tipo_parceria.place(x=170, y=185)
    box_tipo_parceria.bind("<<ComboboxSelected>>")

    # Email
    email_buffet = Label(frame_middle, text="Email : ", font=("Arial 13 bold"), bg="white")
    email_buffet.place(x=10, y=220)
    entry_email_buffet = Entry(frame_middle)
    entry_email_buffet.place(x=80, y=225)


    button_cadastrar = Button(text="Cadastrar", font=("Arial 16 bold"), command=registrar)
    button_cadastrar.place(x=150, y=430)


    window_register_buffet.mainloop()

buffet()
