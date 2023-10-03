from tkinter import Tk, Label, Button, Entry, messagebox, ttk
from Components.Frames import frame_top

def registrarBuffet():
    window = Tk()
    window.geometry("450x500")
    window.resizable(False, False)
    window.title("Registrar Buffet")

    # Frame superior
    frameT = ttk.Frame(window, width=450, height=100, style="Blue.TFrame")
    frameT.grid(row=0, column=0)

    label_title = Label(frameT, text="Registrar Buffet", font=("Arial 30 bold"), bg="white", fg="black")
    label_title.place(x=50, y=25)

    # Largura comum para todos os campos de entrada
    entry_width = 25

    # Labels e campos de entrada
    label_nome = Label(window, text="Nome:", font=("Arial 15 bold"))
    label_nome.place(x=50, y=120)
    entry_nome = Entry(window, width=entry_width)
    entry_nome.place(x=180, y=125)

    label_cnpj = Label(window, text="CNPJ:", font=("Arial 15 bold"))
    label_cnpj.place(x=50, y=150)
    entry_cnpj = Entry(window, width=entry_width)
    entry_cnpj.place(x=180, y=155)

    label_endereco = Label(window, text="Endereço:", font=("Arial 15 bold"))
    label_endereco.place(x=50, y=180)
    entry_endereco = Entry(window, width=entry_width)
    entry_endereco.place(x=180, y=185)

    label_tempo_parceria = Label(window, text="Tempo de Parceria:", font=("Arial 15 bold"))
    label_tempo_parceria.place(x=50, y=210)
    entry_tempo_parceria = Entry(window, width=entry_width)
    entry_tempo_parceria.place(x=245, y=215)

    tipo_buffet = [
        "Parceiro", "Associado"
    ]

    label_tipo_buffet = Label(window, text="Tipo de Buffet:", font=("Arial 15 bold"))
    label_tipo_buffet.place(x=50, y=240)
    combo_tipo_buffet = ttk.Combobox(window, values=tipo_buffet, width=entry_width)
    combo_tipo_buffet.place(x=200, y=245)

    label_email = Label(window, text="Email:", font=("Arial 15 bold"))
    label_email.place(x=50, y=270)
    entry_email = Entry(window, width=entry_width)
    entry_email.place(x=180, y=275)

    button_salvar = Button(window, text="Salvar", font=("Arial 20 bold"))
    button_salvar.place(x=175, y=330)

    window.mainloop()

registrarBuffet()
