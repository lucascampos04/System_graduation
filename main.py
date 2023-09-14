from tkinter import Button, Frame, Tk, messagebox, Label, simpledialog, filedialog
import random





'''colors'''
whitesmoke = "#dcdee8"
whiteBg = "#e6e7eb"
blackLight = "#3d3f47"
blackButLight = "#585959"
blue = "#213ac4"

def number_random():
    number = random.choice(1000, 90000)


def create_business():
    name_business = simpledialog.askstring("Nome da empresa ", "Nome da empresa")
    cnpj_business = simpledialog.askinteger("CNPJ", "CNPJ")
    endereco_business = simpledialog.askstring("Endereço ", "Endereço")

def brand_graduation():
    name_course = simpledialog.askstring("Nome do curso ", "Nome do curso ")
    name_faculty = simpledialog.askstring("Nome da faculdade", "Nome da faculdade")
    name_people = simpledialog.askstring("Nome do representante ", "Nome do representante")
    phone_people = simpledialog.askinteger("Numero do representante ", "Numero do representante ")
    form_payment = simpledialog.askstring("Forma de pagamento", "Forma de pagamento")
    value_payment = messagebox.showinfo("Valor a ser pago", number_random)




'''WINDOW WHERE BE OPTIONS OF EVENTS E CREATE BUSINESS'''
window = Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("Tela principal")

'''FRAMES'''
frame_top = Frame(window, width=500, height=50, bg=blue)
frame_top.grid(row=0, column=0)

frame_midle = Frame(window, width=500, height=420, bg=whiteBg)
frame_midle.grid(row=1, column=0)

framme_footer = Frame(window, width=500, height=35, bg=blue)
framme_footer.grid(row=2, column=0)

'''LABELS'''
title_frame_top = Label(frame_top, text="Escolha as opções abaixo".upper(), font=("Arial 15 bold"), bg=blue)
title_frame_top.place(x=90, y=10)


'''BUTTONS'''
btn_create_business = Button(frame_midle, text="Criar empresa", font=("Ivy 17 bold"), relief='ridge', command=create_business)
btn_create_business.place(x=20, y=50)

btn_brand_graduation = Button(frame_midle, text="Marca formatura", font=("Ivy 17 bold"), relief='ridge', command=brand_graduation)
btn_brand_graduation.place(x=20, y=130)

btn_defer_graduation = Button(frame_midle, text="Adiar formatura", font=("Ivy 17 bold"), relief='ridge')
btn_defer_graduation.place(x=20, y=210)

btn_official = Button(frame_midle, text="Funcionario", font=("Ivy 17 bold"), relief='ridge')
btn_official.place(x=20, y=290)






window.mainloop()
