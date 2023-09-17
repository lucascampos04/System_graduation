from tkinter import Button, Frame, Tk, Label, simpledialog, ttk, messagebox
from database_connect import connect_database
from inseririDadosRepresentante import inserir_name_representante, inserir_telefone_representante, inserir_forma_de_pagamento_representante, inserir_email_representante
from brand_graduation import brand_graduation

# Declaração das variáveis globais
btn_name_representante = None
btn_telefone_representante = None
combo_form_pagamento = None
label_forma_de_pagamento_escolhida = None
btn_email_representante = None

name_saved = None
telefone_saved = None
frm_pag_escolhida = None
email_saved = None

def inserir_name():
    global name_saved
    name_saved = simpledialog.askstring("Inserir nome", "Insira seu nome")
    btn_name_representante.config(text=f'Nome de representante: {name_saved}')

def inserir_telefone():
    global telefone_saved
    telefone_saved = simpledialog.askstring("Inserir telefone", "Insira seu telefone")
    btn_telefone_representante.config(text=f'Telefone de representante: {telefone_saved}')

def inserir_formas_pagamento(event):
    global frm_pag_escolhida
    frm_pag_escolhida = combo_form_pagamento.get()
    label_forma_de_pagamento_escolhida.config(text=f'Forma de pagamento: {frm_pag_escolhida}')
    label_forma_de_pagamento_escolhida.place(x=25, y=160)

def inserir_email():
    global email_saved
    email_saved = simpledialog.askstring("Inserir email", "Insira seu email")
    btn_email_representante.config(text=f'Email registrado: {email_saved}')

def registrar():
    global name_saved, telefone_saved, frm_pag_escolhida, email_saved

    if name_saved is None or telefone_saved is None or frm_pag_escolhida is None or email_saved is None:
        messagebox.showerror("Error", "Por favor, preencha todos os campos")
        return

    inserir_name_representante(name_saved)
    inserir_telefone_representante(telefone_saved)
    inserir_forma_de_pagamento_representante(frm_pag_escolhida)
    inserir_email_representante(email_saved)

    if name_saved and telefone_saved and frm_pag_escolhida and email_saved:
        brand_graduation()

def representante_criar():
    global frame_midle, btn_name_representante, btn_telefone_representante, combo_form_pagamento, label_forma_de_pagamento_escolhida, btn_email_representante

    window = Tk()
    window.geometry("470x400")
    window.resizable(False, False)
    window.title("Criar representante de classe")

    frame_top = Frame(window, width=470, height=100, bg="black")
    frame_top.grid(row=0, column=0)

    frame_midle = Frame(window, width=470, height=300)
    frame_midle.grid(row=1, column=0)

    label_title_frame_top = Label(frame_top, text="ANTES VOCÊ TERÁ QUE REGISTRAR\nUM\nREPRESENTANTE DE CLASSE", bg="black", fg="white", font=("Arial 15 bold"))
    label_title_frame_top.place(x=35, y=10)

    label_name_representante = Label(frame_midle, text="Nome do representante", font=("Arial 12 bold"))
    label_name_representante.place(x=25, y=20)

    btn_name_representante = Button(frame_midle, text="Clique Aqui! Coloque seu nome.", relief='flat', command=inserir_name)
    btn_name_representante.place(x=25, y=45)

    label_telefone = Label(frame_midle, text="Número do representante", font=("Arial 12 bold"))
    label_telefone.place(x=255, y=20)

    btn_telefone_representante = Button(frame_midle, text="Clique Aqui! Coloque seu telefone.", relief='flat', command=inserir_telefone)
    btn_telefone_representante.place(x=255, y=45)

    label_form_pagamento = Label(
        frame_midle, 
        text="Forma de pagamento",
        font=("Arial", 12, "bold"),
    )
    label_form_pagamento.place(x=25, y=100)

    formas = [
        "PIX",
        "BOLETO",
        "DEBITO",
        "CREDITO",
        "DINHEIRO",
    ]

    combo_form_pagamento = ttk.Combobox(frame_midle, values=formas)
    combo_form_pagamento.place(x=25, y=140)
    combo_form_pagamento.bind("<<ComboboxSelected>>", inserir_formas_pagamento)

    label_forma_de_pagamento_escolhida = Label(frame_midle, text="", font=("Arial", 12, "bold"))
    label_forma_de_pagamento_escolhida.place(x=25, y=170)

    label_email = Label(frame_midle, text="Email do representante", font=("Arial 12 bold"))
    label_email.place(x=255, y=100)

    btn_email_representante = Button(frame_midle, text="Clique Aqui! Coloque seu email.", relief='flat', command=inserir_email)
    btn_email_representante.place(x=255, y=140)

    btn_registrar = Button(frame_midle, text="REGISTRAR", relief='flat', command=registrar, font=("Arial 20 bold"))
    btn_registrar.place(x=140, y=200)

    window.mainloop()

representante_criar()
