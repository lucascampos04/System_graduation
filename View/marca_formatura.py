from tkinter import Tk, Label, Button, Entry, ttk, Radiobutton, StringVar
from Components.Frames import (frame_meio, frame_final, frame_top)
from Model.Query.tablesassoiacao import (insertNameFaculdade,
                                         insertNameCurso,
                                         insertNameEvento,
                                         insertNameStatus,
                                         insertNameForma,
                                         )
from Model.Query.tableFormatura import insertFormatura



# Get
def getfaculdade():
    global  Faculdade
    faculdade = input_faculdade.get()
    return faculdade

def getCurso():
    global getcurso
    getcurso = input_curso.get()
    return getcurso

def getRepresentante():
    global representante
    representante = input_representante.get()
    return representante

def getLimitePessoas():
    global limitepessoas
    limitepessoas = input_limite_pessoas.get()
    return limitepessoas

def getFormaPagamento():
    global formapagamento
    formapagamento = formas_pagamentos.get()
    return formapagamento

def getTipoEvento():
    global tipoevento
    tipoevento = var.get()
    return tipoevento

'''
    def getTotal():
    global total
    total = label_total.get()
    return total
'''

def insert():
    global label_total, new_label
    faculdade = getfaculdade()
    curso = getCurso()
    representante = getRepresentante()
    formapagamento = getFormaPagamento()
    tipoevento = getTipoEvento()
    limitepessoas = getLimitePessoas()

    id_faculdade = insertNameFaculdade(faculdade)
    id_curso = insertNameCurso(curso)
    id_formPagamento = insertNameForma(formapagamento)
    id_tipoEvento = insertNameEvento(tipoevento)

    total = 1000

    insertFormatura(id_faculdade, id_curso, representante, id_formPagamento, total, id_tipoEvento, limitepessoas)
def marca_graduation():
    global input_faculdade, input_curso, input_representante, input_limite_pessoas, formas_pagamentos,var, label_total

    window = Tk()
    window.title("Marca formatura")
    window.geometry("870x600")

    frameT = frame_top(window, 870, 150, '#1e43bd')
    frameT.grid(row=0, column=0)

    frameM = frame_meio(window, 870, 400, 'white')
    frameM.grid(row=1, column=0)

    frameF = frame_final(window, 870, 50, 'white')
    frameF.grid(row=2, column=0)

    # Frame e botões

    # Frame top
    title_frame_top = Label(frameT, text="Marca Formatura", font=("Arial 30 bold"), bg='#1e43bd', fg='black')
    title_frame_top.place(x=30, y=50)

    # Faculdade

    name_faculdade = Label(frameM, text="Faculdade : ", font=("Arial 15 bold"), bg='white')
    name_faculdade.place(x=20, y=50)
    input_faculdade = Entry(frameM)
    input_faculdade.place(x=138, y=58)

    # Curso
    name_curso = Label(frameM, text="Curso : ", font=("Arial 15 bold"), bg='white')
    name_curso.place(x=20, y=100)
    input_curso = Entry(frameM)
    input_curso.place(x=100, y=108)

    # representante
    name_representante = Label(frameM, text="Representante : ", font=("Arial 15 bold"), bg='white')
    name_representante.place(x=20, y=150)
    input_representante = Entry(frameM)
    input_representante.place(x=180, y=158)

    # Formas de pagamento
    formas = [
        "Debito", "Credito",
        "Pix", "Boleto", "Dinheiro"
    ]
    formas_ePagamento_label = Label(frameM, text="Formas de pagamentos", font=("Arial 14 bold"), bg='white')
    formas_ePagamento_label.place(x=20, y=200)
    formas_pagamentos = ttk.Combobox(frameM, values=formas)
    formas_pagamentos.place(x=250, y=206)

    # Duração
    tempo = [
        "10 horas", "5 horas",
        "8 horas", "5 horas"
    ]
    duracao_label = Label(frameM, text="Duração : ", font=("Arial 14 bold"), bg='white')
    duracao_label.place(x=20, y=250)
    duracao = ttk.Combobox(frameM, values=tempo)
    duracao.place(x=130, y=255)

    # Evento publico ou fechado
    label_name_evento = Label(frameM, text="Tipo do evento : ", font=("Arial 14 bold"), bg='white')
    label_name_evento.place(x=550, y=50)

    var = StringVar()

    radio_publico = Radiobutton(frameM, text="Publico", variable=var, value="Publico", bg='white')
    radio_publico.place(x=710, y=60)

    radio_fechado = Radiobutton(frameM, text="Fechado", variable=var, value="Publico", bg='white')
    radio_fechado.place(x=710, y=80)

    # Limite de pessoas
    label_limite_pessoas = Label(frameM, text="Limite de pessoas : ", font=("Arial 14 bold"), bg='white')
    label_limite_pessoas.place(x=480, y=120)

    input_limite_pessoas = Entry(frameM)
    input_limite_pessoas.place(x=680, y=125)

    # Endereços
    label_endereco = Label(frameM, text="Endereços : ", font=("Arial 14 bold"), bg='white')
    label_endereco.place(x=550, y=190)

    rua = StringVar()

    radio_endereco_1 = Radiobutton(frameM, text="Rua ABC, 123", variable=rua, value="rua", bg='white')
    radio_endereco_1.place(x=680, y=196)

    radio_endereco_2 = Radiobutton(frameM, text="Rua XXX, 666", variable=rua, value="rua", bg='white')
    radio_endereco_2.place(x=680, y=220)

    radio_endereco_3 = Radiobutton(frameM, text="Rua HZS, 132", variable=rua, value="rua", bg='white')
    radio_endereco_3.place(x=680, y=244)

    # Data
    datas =[
        "29/06/2023",
        "19/12/2025",
        "20/01/2021",
    ]

    label_datas_disponiveis = Label(frameM, text="Datas disponiveis : ", font=("Arial 14 bold"), bg='white')
    label_datas_disponiveis.place(x=480, y=300)

    options_datas = ttk.Combobox(frameM, values=datas)
    options_datas.place(x=680, y=308)


    # LABEL
    label_total = Label(frameM, text="Total : XXXXXXX", font=("Arial 14 bold"), bg='white')
    label_total.place(x=30, y=300)

    # botão registrar
    btn_registrar = Button(frameM, text="Registrar", font=("Ivy 18 bold"), bg='black', fg='white', command=insert)
    btn_registrar.place(x=30, y=350)

    window.mainloop()

marca_graduation()