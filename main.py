from tkinter import Button, Frame, Tk, messagebox, Label, simpledialog, filedialog

from brand_graduation import brand_graduation
from criar_representante import representante_criar

'''colors'''
whitesmoke = "#dcdee8"
whiteBg = "#e6e7eb"
blackLight = "#3d3f47"
blackButLight = "#585959"
blue = "#213ac4"

def marca_formatura():
    representante_criar()
       


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

'''LABEL NAME OF BUSiNESS'''
name_business = Label(frame_midle, text="Empresa de cerimonias", font=("Arial 30 bold"), bg=whiteBg)
name_business.place(x=20, y=50)

'''BUTTONS'''

'''BUTTTTON OF BRAND GRADUATION (EVENT) '''
brand_graduation = Button(frame_midle, text="Marca formatura", font=("Arial 12 bold"), width=20, command=marca_formatura)
brand_graduation.place(x=20, y=150)

'''BUTTTON OF POSTPONE GRADUATION (EVENT)'''
postpone_graduation = Button(frame_midle, text="Adiar formatura", font=("Arial 12 bold"), width=20)
postpone_graduation.place(x=20, y=200)

'''INFORMATION BUFFET'S THAT IS WORKING IN EVENT'''
info_buffets = Button(frame_midle, text="Registrar buffet", font=("Arial 12 bold"), width=20)
info_buffets.place(x=250, y=150)

'''INFORMATION OF BUSINESS RESPONSIBLE FOR THE GRADUATION (EVENT)'''
info_business = Button(frame_midle, text="Informações da empresa responsavel pelo evento", relief='flat', bg=whiteBg,)
info_business.place(x=95, y=400)


'''CONTACT'''
contact_ = Button(framme_footer, text="Suporte", relief='flat', bg=blue, font=("Arial 15 bold"))
contact_.place(x=370, y=-2)


window.mainloop()
