from tkinter import Tk, Label, Button
from Components.Frames import frame_top, frame_meio, frame_final
from View.marca_formatura import marca_graduation

def marca():
    print("Foi")

def open_window_marca_formatura():
    marca_graduation()

window = Tk()
window.title("Tela inicial")
window.geometry("500x600")
window.resizable(False, False)

 # Frames

frameT = frame_top(window, 500, 150, 'black')
frameT.grid(row = 0, column = 0)

frameM = frame_meio(window, 500, 400, 'white')
frameM.grid(row = 1, column = 0)

frameF = frame_final(window, 500, 50, 'black')
frameF.grid(row = 2, column = 0)

# Labes e Buttons

# frame top
title_frame_top = Label(frameT, text="Empresa de Cerimonias", font=("Arial 30 bold"), bg='black', fg='white')
title_frame_top.place(x=30, y=50)

# frame meio
btn_marca_formatura = Button(frameM,text="Marca Formatura", bg='white', fg='black',width=15, font=("Arial 16 bold"), command=open_window_marca_formatura)
btn_marca_formatura.place(x=10, y=80)

btn_funcionarios = Button(frameM, text="Funcionarios" , bg="white", fg="black",width=15, font=("Arial 16 bold"))
btn_funcionarios.place(x=10, y=190)

btn_buffet = Button(frameM, text="Buffet" , bg="white", fg="black",width=15, font=("Arial 16 bold"))
btn_buffet.place(x=280, y=80)

window.mainloop()