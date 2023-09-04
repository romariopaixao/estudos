from tkinter import *

janela = Tk()
janela.title('Entry')
janela.geometry('350x350')

entry = Entry(janela, width=10)
entry.grid(row=0, column=0)

janela.mainloop()