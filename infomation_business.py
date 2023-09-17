from tkinter import Button, Frame, Tk, messagebox, Label, simpledialog, filedialog
import mysql.connector
import webbrowser

from infoBusinessRepository import get_name, get_email, get_phone, get_ende

'''colors'''
whitesmoke = "#dcdee8"
whiteBg = "#e6e7eb"
blackLight = "#3d3f47"
blackButLight = "#585959"
blue = "#213ac4"


def link_pag():
    url = "https://www.4devs.com.br/gerador_de_cnpj"
    webbrowser.open(url)

def window_info_business(id):
    business_name = get_name(id)
    business_email = get_email(id)
    business_phone = get_phone(id)
    business_ende = get_ende(id)

    window = Tk()
    window.title("Informações da empresa")
    window.resizable(False, False)
    window.geometry("250x400")


    '''FRAMES'''
    frame_top = Frame(window, width=250, height=150, bg=blue)
    frame_top.grid(row=0, column=0, sticky="w")

    frame_midle = Frame(window, width=250, height=250, bg=whitesmoke)
    frame_midle.grid(row=1, column=0, sticky="w")

    '''LABEL'''
    get_name_business = Label(frame_top, text=business_name, font=("Arial 25 bold"), bg=blue, fg="white")
    get_name_business.place(x=10, y=50)

    get_ende_business = Label(frame_midle, text=f'Email : {business_email}' , bg=whitesmoke, font=("Arial 12 bold"))
    get_ende_business.place(x=5, y=30)

    get_phone_business = Label(frame_midle, text=f'Telefone : {business_phone}' , bg=whitesmoke, font=("Arial 12 bold"))
    get_phone_business.place(x=5, y=70)

    get_ende_business = Label(frame_midle, text=f'Endereço : {business_ende}' , bg=whitesmoke, font=("Arial 12 bold"))
    get_ende_business.place(x=5, y=110)

    button_vist_pag = Button(frame_midle, text="Viste nossa pagina", font=("Arial 15 bold"), relief="flat", bg=whitesmoke, command=link_pag)
    button_vist_pag.place(x=10, y=180)

    window.mainloop()

