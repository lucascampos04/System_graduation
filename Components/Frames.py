from tkinter import Frame


def frame_top(janela, width, height, color):
    frameTop = Frame(janela, width=width, height=height, bg=color)
    return  frameTop

def frame_meio(janela, width, height, color):
    frameMeio = Frame(janela, width=width, height=height, bg=color)
    return  frameMeio

def frame_final(janela, width, height, color):
    frameFinal = Frame(janela, width=width, height=height, bg=color)
    return  frameFinal