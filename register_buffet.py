from tkinter import Button, Frame, Tk, Label


def buffet():
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

    name_buffet = Label(frame_middle, text="Nome : ", font=)




    window_register_buffet.mainloop()

buffet()
