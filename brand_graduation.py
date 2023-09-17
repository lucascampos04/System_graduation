from tkinter import (
    messagebox, 
    simpledialog, 
    Tk, 
    Frame, 
    Label, 
    Button, 
    Entry, 
    ttk,
    filedialog,)

from insertDataSchoolRepository import (
    inserir_name_school,
    inserir_name_curse,
    inserir_select_date,
    inserir_endereco,
    inserir_duracao_prevista,
    inserir_tipo_evento,
)

from tkcalendar import Calendar


def inserir_nome_faculdade():
    nome_faculdade = simpledialog.askstring("Inserir nome", "Digite o nome da Faculdade")
    if nome_faculdade:
        inserir_name_school(nome_faculdade)
        button_inserir_nome_faculdade.config(
            text=nome_faculdade,
            font=("Arial", 15, "bold"),
            command=None,
            relief='flat',
            bg="blue",
        )

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

    label_data_selecionada = Label(
        frame_midle,
        text=f"Data selecionada: {data_selecionada}",
        font=("Arial", 10, "bold"),
        bg="blue",
        fg="black",
    )
    label_data_selecionada.place(x=170, y=141)



def selecionar_ende(event):
    global adress_selecionado
    adress_selecionado = combo_ende.get()

    # remove o endereço selecionado do combos
    combo_ende.set("")
    combo_ende["values"] = [addr for addr in adress if addr != adress_selecionado]

    # encontre o índice do endereço selecionado na lista de endereços
    index = adress.index(adress_selecionado)
    ponto_referencia = pontos_referencia[index]

    inserir_endereco(adress_selecionado, ponto_referencia)
    
    label_ende_selecionada = Label(
        frame_midle,
        text=f"Endereço selecionado: {adress_selecionado}",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="black",
    )
    label_ende_selecionada.place(x=20, y=250)

    label_ponto_referencia = Label(
        frame_midle,
        text=f"Ponto de referência: {ponto_referencia}",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="black",
    )
    label_ponto_referencia.place(x=20, y=270)



def hours_disponiveis(event):
    global hours_dispo_selecionada
    hours_dispo_selecionada = combo_hrs.get()
    inserir_duracao_prevista(hours_dispo_selecionada)

    combo_hrs.set("")
    combo_hrs["values"] = [hr for hr in hours if hr != hours_dispo_selecionada]

    label_hrs_selecionada = Label(
        frame_midle,
        text=f"Horario selecionado: \n{hours_dispo_selecionada}",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="black",
    )
    label_hrs_selecionada.place(x=480, y=170)
    
def tipo_evento(event):
    global tipo_evento_selecionado, label_limit_convidado

    tipo_evento_selecionado = combo_tipo_evento.get()
    

    combo_tipo_evento.set("")
    combo_tipo_evento["values"] = [tp_event for tp_event in tipo_event if tp_event != tipo_evento_selecionado]

    # Mensagem falando o tipo do evento
    label_tip_event_selecionada = Label(
        frame_midle,
        text=f"O evento é : {tipo_evento_selecionado}",
        font=("Arial", 11, "bold"),
        bg="blue",
        fg="black",
    )
    label_tip_event_selecionada.place(x=530, y=290)

    # se for "FECHADO" vai pedir o limite de convidados
    if tipo_evento_selecionado == "FECHADO":
        limite_convidados = simpledialog.askinteger("Limite de Convidados", "Digite o limite de convidados:")
        label_limit_convidado = Label(
            text=f"Limite de convidados: {limite_convidados}",
            font=("Arial", 11, "bold"),
            bg="blue",
            fg="white",
        )
        label_limit_convidado.place(x=520, y=460)
        
    inserir_tipo_evento(tipo_evento_selecionado, limite_convidados)


def brand_graduation():
    global tipo_evento_selecionado, limite_convidados
    limite_convidados = None
    window = Tk()
    window.title("Marca formatura")
    window.resizable(False, False)
    window.geometry("800x550")

    '''FRAMES'''
    global frame_midle
    frame_top = Frame(window, width=800, height=150, bg="black")
    frame_top.grid(row=0, column=0)

    frame_midle = Frame(window, width=800, height=400, bg="blue")
    frame_midle.grid(row=1, column=0)

    title_branda_graduation = Label(
        frame_top,
        text="MARQUE SUA FORMATURA",
        font=("Arial", 16, "bold"),
        bg="black",
        fg="white",
    )
    title_branda_graduation.place(x=10, y=70)

    # Nome da faculdade

    label_name_school = Label(
        frame_midle,
        text="Nome da Universidade",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
    label_name_school.place(x=20, y=25)

    global button_inserir_nome_faculdade
    button_inserir_nome_faculdade = Button(
        frame_midle,
        text="Clique aqui e digite o nome da Faculdade",
        command=inserir_nome_faculdade,
        font=("Arial", 12),
        relief='flat',
        bg="blue",
        fg="white",
    )
    button_inserir_nome_faculdade.place(x=20, y=60)

    # Nome do curso

    label_name_curse = Label(
        frame_midle,
        text="Nome do curso",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
    label_name_curse.place(x=520, y=25)

    global button_inserir_nome_curso
    button_inserir_nome_curso = Button(
        frame_midle,
        text="Clique aqui e digite o nome do curso",
        command=inserir_nome_curso,
        font=("Arial", 12),
        relief='flat',
        bg="blue",
        fg="white",
    )
    button_inserir_nome_curso.place(x=520, y=60)

    # Escolher uma data

    label_select_date = Label(
        frame_midle,
        text="Escolha uma data",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
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
        "2023-11-22",
    ]

    global combo_date
    combo_date = ttk.Combobox(frame_midle, values=datas)
    combo_date.place(x=20, y=140)
    combo_date.bind("<<ComboboxSelected>>", selecionar_data)

    # Escolher um endereço
    label_select_ende = Label(
        frame_midle,
        text="Escolha um endereço",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
    label_select_ende.place(x=20, y=180)

    global adress
    adress = [
        "Rua A, 123",
        "Avenida B, 456",
        "Praça C, 789",
        "Alameda D, 101",
        "Travessa E, 202",
    ]

    global pontos_referencia
    pontos_referencia = [
        "Próximo à praça central",
        "Ao lado do mercado",
        "Em frente ao parque",
        "Próximo à escola",
        "Na esquina do restaurante",
    ]

    global combo_ende
    combo_ende = ttk.Combobox(frame_midle, values=adress)
    combo_ende.place(x=20, y=220)
    combo_ende.bind("<<ComboboxSelected>>", selecionar_ende)

    # selecione uma duração prevista
    label_hrs_select = Label(
        frame_midle, 
        text="Horarios disponiveis",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
    label_hrs_select.place(x=520, y=100)


    global hours
    hours = [
        "Começa 09:00 horas e acaba às 12:00 horas",
        "Começa 14:30 horas e acaba às 16:30 horas",
        "Começa 17:00 horas e acaba às 19:00 horas",
        "Começa 20:00 horas e acaba às 23:00 horas",
    ]

    global combo_hrs
    combo_hrs = ttk.Combobox(frame_midle, values=hours, width=40)
    combo_hrs.place(x=520, y=140)
    combo_hrs.bind("<<ComboboxSelected>>", hours_disponiveis)

    # selecione se o evento é aberto ou fechado
    global label_event_tip
    label_event_tip = Label(
        frame_midle, 
        text="Evento aberto ou fechado",
        font=("Arial", 14, "bold"),
        bg="blue",
        fg="white",
    )
    label_event_tip.place(x=520, y=220)


    global tipo_event
    tipo_event = [
        "ABERTO", "FECHADO"
    ]

    global combo_tipo_evento
    combo_tipo_evento = ttk.Combobox(frame_midle, values=tipo_event, width=40)
    combo_tipo_evento.place(x=520, y=260)
    combo_tipo_evento.bind("<<ComboboxSelected>>", tipo_evento)


    window.mainloop()

brand_graduation()
