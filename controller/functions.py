import random
from tkinter import messagebox, simpledialog

def number_random():
    number = random.choice(1000, 90000)


def methhod_brand_graduation():
    name_course = simpledialog.askstring("Nome do curso ", "Nome do curso ")
    name_faculty = simpledialog.askstring("Nome da faculdade", "Nome da faculdade")
    name_people = simpledialog.askstring("Nome do representante ", "Nome do representante")
    phone_people = simpledialog.askinteger("Numero do representante ", "Numero do representante ")
    form_payment = simpledialog.askstring("Forma de pagamento", "Forma de pagamento")
    value_payment = messagebox.showinfo("Valor a ser pago", number_random)