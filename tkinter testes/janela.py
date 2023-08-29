from tkinter import *

#cores
cor1 = '#242323' #preta


janela = Tk()
janela.title('Ola mundo')#titulo da janela
janela.geometry('800x750')#tamanho da janela, primeiro largura, segundo altura

#config tem varias funçõs referente a cor, bordar, tamanho de borda e etc da janela. Verificar
#as opção na documentação ou no proprio metodo. No exemplo abaixo muderemos a cor de fundo(bg=#242323)
janela.config(bg=cor1)

#Alterando o logo do janela: False para desativar a logo padrao > Photoimagem passando o caminho da img
janela.iconphoto(False, PhotoImage(file='logo.png'))

janela.resizable(width=False, height=False)#Bloquenado a manipulação do tamanho da janela



janela.mainloop()#mainloop deixa a janela rodando constaimente, sem esse metodo, a janela nao abre